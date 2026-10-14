use pulldown_cmark::{Event, Options, Parser};
use std::io::Read;

fn math(text: &str) -> Vec<String> {
    Parser::new_ext(text, Options::ENABLE_MATH)
        .filter_map(|event| match event {
            Event::InlineMath(m) | Event::DisplayMath(m) => Some(m.to_string()),
            _ => None,
        })
        .collect()
}

fn tokens(latex: &str) -> Vec<&str> {
    let mut out = Vec::new();
    let mut rest = latex;
    while let Some(c) = rest.chars().next() {
        let len = match c {
            '\\' => match rest[1..].chars().next() {
                Some(a) if a.is_ascii_alphabetic() => {
                    1 + rest[1..]
                        .find(|x: char| !x.is_ascii_alphabetic())
                        .unwrap_or(rest.len() - 1)
                }
                Some(a) => 1 + a.len_utf8(),
                None => 1,
            },
            c => c.len_utf8(),
        };
        let token = &rest[..len];
        let spacing = matches!(token, "\\," | r"\;" | "\\:" | "\\!" | "\\ " | "~");
        if !(c.is_whitespace() || spacing || token == "{" || token == "}") {
            out.push(token);
        }
        rest = &rest[len..];
    }
    out
}

fn occurs(symbol: &str, math: &[String]) -> bool {
    let wanted = tokens(symbol);
    !wanted.is_empty()
        && math
            .iter()
            .any(|m| tokens(m).windows(wanted.len()).any(|w| w == wanted))
}

fn claims(node: &serde_json::Value, out: &mut Vec<String>) {
    out.push(node["claim"].as_str().unwrap().to_string());
    if let Some(cs) = node["children"].as_array() {
        for c in cs {
            claims(c, out);
        }
    }
}

fn visit(node: &serde_json::Value, bad: &mut usize) {
    let id = node["id"].as_str().unwrap();
    let claim = node["claim"].as_str().unwrap();
    // Count dollar signs vs math spans found, to spot unparsed math.
    let dollars = claim.matches('$').count();
    let spans = math(claim);
    if dollars != spans.len() * 2 {
        println!("{id}: {dollars} dollars but {} math spans: {claim}", spans.len());
        *bad += 1;
    }
    if let Some(adds) = node["adds"].as_array() {
        let mut all = Vec::new();
        claims(node, &mut all);
        let maths: Vec<String> = all.iter().flat_map(|c| math(c)).collect();
        for a in adds {
            let s = a["symbol"].as_str().unwrap();
            if !occurs(s, &maths) {
                println!("{id}: adds {s} not found below");
                *bad += 1;
            }
        }
    }
    if let Some(cs) = node["children"].as_array() {
        for c in cs {
            visit(c, bad);
        }
    }
}

fn main() {
    let mut s = String::new();
    std::io::stdin().read_to_string(&mut s).unwrap();
    let v: serde_json::Value = serde_json::from_str(&s).unwrap();
    let mut bad = 0;
    visit(&v["root"], &mut bad);
    println!("math problems: {bad}");
}
