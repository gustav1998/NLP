# DTU NLP, LLM operations and knowledge graphs — Autumn 2026

5 ECTS, about 10–11 hours weekly. Official sources confirm an individual Python NLP Web-service repository plus examination, pass/fail. Exercises build the components for the project.

## Resume studying

Study notes and progress now live only in the Obsidian vault at `/Users/gustavmoller/Documents/Obsidian/DTU/NLP - Autumn 2026/`. Start with `Study progress.md` and the relevant `Week N.md` note. Open questions are kept in the progress page. Tell the assistant what you tried; help begins with diagnosis and hints unless you request implementation.

## Run the workspace

Core setup is installed and verified: Python/uv, Git, FastAPI/Uvicorn, tests/linting, Docker through Colima and Docker Compose. Environment checks live in `setup/`; exercise implementations live in `exercises/`.

## Where things live

- [Official-source review](course-material/official/review-2026-09-10.md): announcements, email findings, logistics, conflicts and scope of inspection.
- `course-material/official/`: course PDF, introduction/Week 1 slides, original Week 1 Markdown and supplied UI.
- `course-material/notes/`: linked NLP edition dated 18 August 2026 and KG edition dated 31 August 2026; filenames retain 2025/2024.
- `weeks/week-01/` … `weeks/week-13/`: code-oriented exercise pointers using local teaching-week labels.
- `exercises/`: student-written weekly implementations.
- `project/`: candidate ideas and decisions; no project selected.
- [references.md](references.md): source precedence and documentation.
- `/Users/gustavmoller/Documents/Obsidian/DTU/NLP - Autumn 2026/`: progress, concepts, weekly notes, questions and reading notes.

## Remaining gaps

Current Week 3 exercise specification; clarification of quiz requirements; final submission deadline/exam arrangements; 6 November content. Formal registration is confirmed by the 7 September email. Exercise submissions are optional by student clarification.

## Conventions

Python with uv; FastAPI and Docker/Podman/compose as required; small explainable modules, validation and focused tests. Explain dependencies before adding them. Use `.env` for real secrets and never print or commit them; `.env.example` has variable names with empty values only. CampusAI's course-documented base URL is `https://api.campusai.compute.dtu.dk/v1/`; off-campus access requires DTU VPN, and 401 likely means authentication/key trouble. Week 1 forbids external Web services, so CampusAI setup can wait.

Week 2 reading and the PDF-to-sentences exercise are completed. The implementation is in `exercises/week-02-pdf-to-sentences/`.

## Next session

Obtain and inspect the current Week 3 Text-to-person specification before implementing it. The remaining Week 1 image-size/final-review work stays visible in Obsidian as backlog.
