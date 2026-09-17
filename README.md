# DTU NLP, LLM operations and knowledge graphs — Autumn 2026

5 ECTS, about 10–11 hours weekly. Official sources confirm an individual Python NLP Web-service repository plus examination, pass/fail. Exercises build the components for the project. This workspace tracks study and implementation separately; completion requires your explicit confirmation.

## Ready for tomorrow

**Friday 11 September, 08:00–12:00, building 358 room 066, DTU Lyngby.**

Core setup is installed and verified: Python/uv, Git, FastAPI/Uvicorn, tests/linting, Docker through Colima and Docker Compose.

```sh
cd /Users/gustavmoller/Desktop/NLP
./setup/start.sh
```

Open http://127.0.0.1:8765/docs. [Setup details and stop commands](setup/README.md).

Current preference: **student-led Week 1 rebuild from scratch; Week 1 reading completed**. Old assistant solution and ZIP archived under `archive/week-01-assistant-reference/`; old service stopped. Student-written implementation: `exercises/week-01-sentiment/`.

## Resume studying

Open [progress.md](progress.md), the relevant `weeks/week-NN/README.md` and [questions](notes/questions.md). Tell the assistant what you tried; help begins with diagnosis and hints unless you request implementation. Report what you actually completed after studying so the tracker can be updated precisely.

## Run the workspace

Use the startup command above. The environment check lives in `setup/`; actual exercise implementations remain in `exercises/` when requested. The old Week 1 Git repository is archived; the student’s current Week 1 project has its own Git repository. The supplied official UI is preserved as reference.

## Where things live

- [Official-source review](course-material/official/review-2026-09-10.md): announcements, email findings, logistics, conflicts and scope of inspection.
- `course-material/official/`: course PDF, introduction/Week 1 slides, original Week 1 Markdown and supplied UI.
- `course-material/notes/`: linked NLP edition dated 18 August 2026 and KG edition dated 31 August 2026; filenames retain 2025/2024.
- `weeks/week-01/` … `weeks/week-13/`: local teaching-week labels excluding the 16 October break.
- `exercises/`: working implementations when requested; `notes/concepts/` and `notes/weekly/`: study aids/reflections.
- `project/`: candidate ideas and decisions; no project selected.
- [references.md](references.md): source precedence and documentation.

## Remaining gaps

Week 2 deadline and OCR/body-selection expectations; verified download/content of the official project-proposals.md; clarification of exercise/quiz hand-in labels; final submission deadline/exam arrangements; 6 November content. Formal registration is confirmed by the 7 September email. Week 1 reading is confirmed completed; exercise remains partly completed.

## Conventions

Python with uv; FastAPI and Docker/Podman/compose as required; small explainable modules, validation and focused tests. Explain dependencies before adding them. Use `.env` for real secrets and never print or commit them; `.env.example` has variable names with empty values only. CampusAI's course-documented base URL is `https://api.campusai.compute.dtu.dk/v1/`; off-campus access requires DTU VPN, and 401 likely means authentication/key trouble. Week 1 forbids external Web services, so CampusAI setup can wait.

Week 2 material is now supplied: [requirements and preparation](weeks/week-02/README.md). Eight originals saved; Week 2 prototype work is partly completed; reading remains unconfirmed.

## Next session

Week 1: four tests passed and student-built container served the API. Start by checking the image size, then review/document/package the student’s own work. See [session record](notes/weekly/2026-09-11-progress.md).
