"""Aggregate-only Matplotlib charts for the MySQL demonstration database."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def _bar_chart(connection, sql, title, filename, x_label, y_label):
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()

    labels = [str(row[0]) for row in rows]
    values = [float(row[1]) for row in rows]
    output = Path("charts_output")
    output.mkdir(exist_ok=True)

    figure, axis = plt.subplots(figsize=(9, 5))
    if rows:
        axis.bar(labels, values, color="#4c78a8")
        axis.tick_params(axis="x", labelrotation=25)
    else:
        axis.text(0.5, 0.5, "No data available yet", ha="center", va="center")
        axis.set_xticks([])
        axis.set_yticks([])
    axis.set_title(title)
    axis.set_xlabel(x_label)
    axis.set_ylabel(y_label)
    figure.tight_layout()
    path = output / filename
    figure.savefig(path, dpi=140)
    plt.close(figure)
    return path


def generate_charts(connection):
    """Create four charts from counts and totals, never individual child records."""
    queries = [
        (
            "SELECT gender, COUNT(*) FROM children GROUP BY gender ORDER BY gender",
            "Children by recorded gender (aggregate)",
            "children_by_gender.png",
            "Recorded gender",
            "Number of demo records",
        ),
        (
            "SELECT status, COUNT(*) FROM admission_applications GROUP BY status ORDER BY status",
            "Admission application workflow",
            "application_status.png",
            "Application status",
            "Number of applications",
        ),
        (
            "SELECT DATE_FORMAT(donated_on, '%Y-%m'), SUM(amount) "
            "FROM donations GROUP BY DATE_FORMAT(donated_on, '%Y-%m') "
            "ORDER BY DATE_FORMAT(donated_on, '%Y-%m')",
            "Donations by month",
            "donations_by_month.png",
            "Month",
            "Amount (demo currency units)",
        ),
        (
            "SELECT category, SUM(amount) FROM expenses GROUP BY category ORDER BY category",
            "Expenses by category",
            "expenses_by_category.png",
            "Category",
            "Amount (demo currency units)",
        ),
    ]
    return [_bar_chart(connection, *query) for query in queries]
