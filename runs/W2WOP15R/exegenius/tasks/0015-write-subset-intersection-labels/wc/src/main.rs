use pulldown_cmark::{Parser, Options, Event};
fn main() {
    let path = std::env::args().nth(1).unwrap();
    let body = std::fs::read_to_string(path).unwrap();
    // strip cites
    let mut text = String::new();
    let mut rest = body.as_str();
    while let Some(i) = rest.find("<cite") {
        text.push_str(&rest[..i]);
        let j = rest[i..].find("</cite>").unwrap() + i + 7;
        rest = &rest[j..];
    }
    text.push_str(rest);
    let mut total = 0;
    for ev in Parser::new_ext(&text, Options::ENABLE_MATH) {
        if let Event::Text(t) = ev {
            let n = t.split_whitespace().count();
            total += n;
            if std::env::args().nth(2).is_some() { println!("{n}\t{:?}", t.to_string()); }
        }
    }
    println!("TOTAL {total}");
}
