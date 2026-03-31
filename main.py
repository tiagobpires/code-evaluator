from analyzer import analyze_code
import typer

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from schemas import CodeReview


app = typer.Typer(
    help="Code evaluator CLI with rich terminal output.",
)
console = Console()


def _render_list(title: str, items: list[str], style: str) -> None:
    content = "\n".join(f"- {item}" for item in items) if items else "- No items"
    console.print(Panel(content, title=title, border_style=style))


def _render_review(review: CodeReview, file_path: str) -> None:
    summary = Table.grid(expand=True)
    summary.add_column(style="bold cyan", width=20)
    summary.add_column()
    summary.add_row("File", file_path)
    summary.add_row("Overall Score", f"{review.general_score}/5")
    summary.add_row("Complexity", review.estimated_complexity)

    console.print(Panel(summary, title="Summary", border_style="cyan"))
    console.print(Panel(review.overall_quality_summary, title="Overview"))
    _render_list("Strengths", review.strengths, "green")
    _render_list("Issues", review.issues, "red")
    _render_list("Improvements", review.improvements, "yellow")


def main():

    file_path = input("File path: ")

    with console.status("Analyzing code...", spinner="dots"):
        review = analyze_code(file_path)

    _render_review(review, file_path)


if __name__ == "__main__":
    main()
