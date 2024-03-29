from datetime import datetime
from art import text2art
import git


def main():
    days = [
        (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3), (9, 3), (10, 3), (13, 3), (16, 3), (17, 3), (20, 3), (23, 3), (24, 3), (30, 3),
        (7, 4), (8, 4), (9, 4), (10, 4), (11, 4), (12, 4), (13, 4), (14, 4), (17, 4), (18, 4), (21, 4), (24, 4), (26, 4), (28, 4), (29, 4), (30, 4),
        (1, 5), (4, 5), (12, 6), (13, 6), (14, 6), (15, 6), (16, 6), (17, 6), (18, 6), (19, 6), (22, 5), (23, 5), (26, 5), (29, 5), (31, 5),
        (2, 6), (3, 6), (4, 6), (5, 6), (8, 6), (16, 6), (17, 6), (18, 6), (19, 6), (20, 6), (21, 6), (22, 6), (23, 6), (29, 6), (30, 6),
        (6, 7), (7, 7), (8, 7), (9, 7), (10, 7), (11, 7), (12, 7), (13, 7), (21, 7), (22, 7), (23, 7), (24, 7), (25, 7), (26, 7), (28, 7), (31, 7),
        (1, 8), (4, 8), (7, 8), (9, 8), (11, 8), (12, 8), (13, 8), (14, 8), (17, 8), (22, 8), (28, 8), (29, 8),
        (3, 9), (5, 9), (9, 9), (12, 9), (15, 9), (16, 9), (17, 9), (18, 9), (19, 9), (20, 9), (21, 9),
        (3, 10), (13, 10), (14, 10), (15, 10), (16, 10), (17, 10), (18, 10), (19, 10), (20, 10), (26, 10), (27, 10),
        (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (21, 11), (27, 11), (28, 11),
        (3, 12), (5, 12), (9, 12), (12, 12), (15, 12), (16, 12), (17, 12), (18, 12), (19, 12), (20, 12), (21, 12), (26, 12)
    ]

    date_actuelle = datetime.now().date()

    if (date_actuelle.day, date_actuelle.month) in days:
        repo = git.Repo("./")
        repo.git.pull()
        day = days.index((date_actuelle.day, date_actuelle.month)) + 1
        readme = "README.md"
        for i in range(4):
            with open(readme, "w") as file:
                file.write("commit - " + str(i))
            repo.git.add(".")
            repo.git.commit("-m", f"Day {day} - {i}")
            origin = repo.remote(name="origin")
            origin.push()
        text_day = text2art("Day " + str(day), "colossal")
        readme_content = "<pre>\n" + text_day + "</pre>"
        with open(readme, "w") as file:
            file.write(readme_content)
        repo.git.add(".")
        repo.git.commit("-m", f"Day {day}")
        origin = repo.remote(name="origin")
        origin.push()


if __name__ == "__main__":
    main()
