"""School bus transport register management system."""
import sqlite3


conn = sqlite3.connect(":memory:")

conn.execute(
    "CREATE TABLE riders ("
    "id INTEGER PRIMARY KEY, "
    "student TEXT, "
    "route TEXT, "
    "stop TEXT, "
    "fee INTEGER)"
)


def enroll_rider(student, route, stop, fee):
    """Register a student on a school bus route."""
    conn.execute(
        "INSERT INTO riders (student, route, stop, fee) "
        "VALUES (?, ?, ?, ?)",
        (student, route, stop, fee)
    )
    conn.commit()


def route_roster(route):
    """Return the names of students assigned to a route."""
    return [
        row[0]
        for row in conn.execute(
            "SELECT student FROM riders WHERE route = ?",
            (route,)
        )
    ]


def export_roster(path, route):
    """Export the student roster of a route to a text file."""
    with open(path, "w", encoding="utf-8") as output_file:
        for name in route_roster(route):
            output_file.write(name + "\n")


def dispatch_alert(route):
    """Display a bus dispatch notification."""
    print(f"Dispatching bus {route}")


def fee_collected(route):
    """Calculate the total fees collected for a route."""
    try:
        result = conn.execute(
            "SELECT SUM(fee) FROM riders WHERE route = ?",
            (route,)
        ).fetchone()

        return result[0] if result[0] is not None else 0

    except sqlite3.Error:
        return 0


def main():
    """Run the school transport register demonstration."""
    enroll_rider("Tara", "R1", "Lake Road", 1800)
    enroll_rider("Kabir", "R1", "Mill Street", 1800)
    enroll_rider("Zoya", "R2", "Fort Gate", 2100)

    if fee_collected("R1") != 3600:
        raise ValueError("Fee collection verification failed.")

    export_roster("route_r1.txt", "R1")
    dispatch_alert("R1")

    print(route_roster("R2"))


if __name__ == "__main__":
    main()
