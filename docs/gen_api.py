from pathlib import Path
import mkdocs_gen_files

src_dir = Path("src/luna")
docs_dir = Path("reference")

with mkdocs_gen_files.open(docs_dir / "index.md", "w") as f:
    print("# API Reference", file=f)
    print("\nThis section contains the API documentation for the `luna` package.", file=f)

for path in src_dir.rglob("*.py"):
    if path.stem == "__init__":
        module_path = path.parent.relative_to("src").with_suffix("")
    else:
        module_path = path.relative_to("src").with_suffix("")

    doc_path = docs_dir / module_path.with_suffix(".md")
    full_module_name = ".".join(module_path.parts)

    with mkdocs_gen_files.open(doc_path, "w") as f:
        print(f"# `{full_module_name}`", file=f)
        print(f"\n::: {full_module_name}", file=f)

    mkdocs_gen_files.set_edit_path(doc_path, path)