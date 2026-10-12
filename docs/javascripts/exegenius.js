(() => {
  const key = "exegenius-refs";
  const apply = shown => document.body.classList.toggle("exegenius-refs-shown", shown);
  const stored = () => {
    try { return localStorage.getItem(key); } catch (e) { return null; }
  };
  const isShown = () => (stored() ?? "hidden") === "shown";
  const setup = () => {
    apply(isShown());
    const article = document.querySelector("article");
    if (!article || !article.querySelector(".exegenius-ref")) return;
    const button = document.createElement("button");
    button.className = "exegenius-ref-toggle";
    const label = () => button.textContent = isShown() ? "Hide sources" : "Show sources";
    label();
    button.addEventListener("click", () => {
      try { localStorage.setItem(key, isShown() ? "hidden" : "shown"); } catch (e) {}
      apply(isShown());
      label();
    });
    article.prepend(button);
  };
  if (typeof document$ !== "undefined") document$.subscribe(setup);
  else document.addEventListener("DOMContentLoaded", setup);
})();
