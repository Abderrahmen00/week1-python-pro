from dataclasses import dataclass
from datetime import date


@dataclass(order=True)
class StudySession:
    subject: str
    duration_minutes: int
    date: date
    topics: list[str]

    def __post_init__(self) -> None:
        if not self.topics or self.duration_minutes < 1:
            raise ValueError(
                "Topics and duration must be provided and duration must be positive"
            )

    @property
    def hours(self) -> float:
        return self.duration_minutes / 60


samples = [
    StudySession("Math", 60, date(2023, 1, 1), ["algebra", "geometry"]),
    StudySession("Science", 90, date(2023, 1, 2), ["biology", "chemistry"]),
    StudySession(
        "History", 45, date(2023, 1, 3), ["ancient civilizations", "modern history"]
    ),
    StudySession("Language", 60, date(2023, 1, 4), ["English", "French", "Arabic"]),
    StudySession("Art", 30, date(2023, 1, 5), ["painting", "sculpture"]),
]
print(samples)

samples.sort(key=lambda s: s.duration_minutes)
print()

print(samples)
