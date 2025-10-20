# Interviewer Platform

The **Interviewer Platform** is a Django-based application designed for conducting automated interviews and simulating interviewee interactions. It integrates transcription, vocalization, and comprehensive interview scripting. Researchers can use this platform to facilitate interviews with participants and then interact with simulated interviewees that are  generated from the interview transcripts. This repository contains the complete source code, configuration, and assets necessary to deploy and run the platform.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Directory Structure](#directory-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

The Interviewer Platform is built to manage and conduct interviews using a combination of automated scripts and real-time agent modules. Its functionality has been expanded upon to simulate interviewee responses based on their interview transcripts, allowing administrators to engage in interactive sessions with these simulations. It leverages Django’s robust framework to deliver a seamless user experience for both interview administrators and participants. Key functionalities include:

- **Interview Scripting:** Define detailed interview modules using JSON scripts.
- **Agent Modules:** Automated agents for transcription and vocalization.
- **User Interface:** A comprehensive set of templates and views for interacting with simulations, managing interviews, user accounts, and settings.
- **Infrastructure:** Ready-to-deploy configurations, with Heroku support (Procfile, Aptfile, runtime.txt), Docker support (Dockerfile, compose.yml) and a structured settings module.

---

## Features

- **Dynamic Interview Scripts:** Customize interview flow with a collection of JSON scripts.
- **Transcription & Vocalization:** Integrated modules (`transcribe.py`, `vocalize.py`) to handle audio processing.
- **Scalable Architecture:** Separation of concerns through modular directory structure (apps, templates, and utilities).
- **User Management:** Full-featured account management with email confirmation, password reset, and social account integration.
- **Deployment Ready:** Includes configuration files for easy deployment to platforms like Heroku.
- **Containerised:** Services are containerised using (`Dockerfile`, `compose.yml`) for a smoother developer experience.
- **Brain Factory:** A new simulation brain can be easily defined by inheriting from the `abstract_brain.py` and incorporated by listing it within the `brain_factory.py`.

---

## Directory Structure

Below is an overview of the repository’s directory structure:

```
gabm_interviewer_platform/
├── Aptfile
├── app.yaml
├── compose.yml
├── db.sqlite3
├── Dockerfile
├── entrypoint.sh
├── global_methods.py
├── google-cred.json
├── manage.py
├── requirements.txt
├── runtime.txt
├── gabm_infra/
│   ├── __init__.py
│   ├── db.sqlite3
│   ├── urls.py
│   ├── wsgi.py
│   └── settings/
│       ├── __init__.py
│       └── base.py
├── interviewer_agent/
│   ├── agent_modules/
│   │   ├── transcribe.py
│   │   ├── transcribe_OLD.py
│   │   ├── transcribe_test.py
│   │   └── vocalize.py
│   ├── interview_script/
│   │   └── new_avp_full_v1/
│   │       ├── meta.json
│   │       ├── module1.json
│   │       ├── module10.json
│   │       ├── module11.json
│   │       ├── module12.json
│   │       ├── module13.json
│   │       ├── module14.json
│   │       ├── module15.json
│   │       ├── module16.json
│   │       ├── module17.json
│   │       ├── module18.json
│   │       ├── module19.json
│   │       ├── module2.json
│   │       ├── module20.json
│   │       ├── module21.json
│   │       ├── module22.json
│   │       ├── module23.json
│   │       ├── module24.json
│   │       ├── module25.json
│   │       ├── module26.json
│   │       ├── module27.json
│   │       ├── module28.json
│   │       ├── module29.json
│   │       ├── module3.json
│   │       ├── module30.json
│   │       ├── module31.json
│   │       ├── module32.json
│   │       ├── module33.json
│   │       ├── module34.json
│   │       ├── module35.json
│   │       ├── module36.json
│   │       ├── module37.json
│   │       ├── module38.json
│   │       ├── module39.json
│   │       ├── module4.json
│   │       ├── module40.json
│   │       ├── module41.json
│   │       ├── module42.json
│   │       ├── module43.json
│   │       ├── module44.json
│   │       ├── module45.json
│   │       ├── module46.json
│   │       ├── module47.json
│   │       ├── module48.json
│   │       ├── module49.json
│   │       ├── module5.json
│   │       ├── module50.json
│   │       ├── module51.json
│   │       ├── module52.json
│   │       ├── module53.json
│   │       ├── module54.json
│   │       ├── module55.json
│   │       ├── module56.json
│   │       ├── module57.json
│   │       ├── module6.json
│   │       ├── module7.json
│   │       ├── module8.json
│   │       └── module9.json
│   ├── interviewer_utils/
│   │   └── settings.py
│   └── prompt_template/
│       ├── __init__.py
│       ├── gpt_structure.py
│       ├── gpt_structure_OLD.py
│       ├── gpt_structure_test.py
│       ├── print_prompt.py
│       ├── run_gpt_prompt.py
│       └── prompts/
│           ├── conditional_v1.txt
│           ├── factualq_next_interview_step_v1.txt
│           ├── factualq_next_interview_step_v2.txt
│           ├── module_notes_v1.txt
│           ├── q_end_thankyou_v1.txt
│           ├── qualitativeq_next_interview_step_v1.txt
│           └── qualitativeq_next_interview_step_v2.txt
├── pages/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── context_processors.py
│   ├── forms.py
│   ├── interview_settings.py
│   ├── models.py
│   ├── pipelines.py
│   ├── tests.py
│   ├── views.py
│   └── migrations/
│       ├── 0001_initial.py
│   │   └── ... (2 more migration files)
├── Procfile
├── README.md
├── sim_brain/
│   ├── brain_factory.py
│   ├── brains/
│   │   ├── __init__.py
│   │   ├── abstract_brain.py
│   │   ├── doppleganger_brain.py
│   │   ├── park_brain.py
│   │   └── silly_brain.py
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   └── ... (5 more migration files)
│   ├── models.py
│   └── templatetags/
│       └── reflection_filters.py
├── static_dirs/
│   ├── gabm/
│   │   ├── img/ ...
│   │   ├── js/ ...
│   │   └── sneat/ ...
│   └── sneat/
│       └── assets/ ...
├── superuser.py
└── templates/
    ├── aside_navbar.html
    ├── base.html
    ├── footer.html
    ├── navbar.html
    ├── account/
    │   ├── account_inactive.html
    │   ├── base.html
    │   ├── email.html
    │   ├── email_change.html
    │   ├── email_confirm.html
    │   ├── login.html
    │   ├── logout.html
    │   ├── password_change.html
    │   ├── password_reset.html
    │   ├── password_reset_done.html
    │   ├── password_reset_from_key.html
    │   ├── password_reset_from_key_done.html
    │   ├── password_set.html
    │   ├── reauthenticate.html
    │   ├── signup.html
    │   ├── signup_closed.html
    │   ├── verification_sent.html
    │   ├── verified_email_required.html
    │   ├── email/
    │   │   ├── account_already_exists_message.txt
    │   │   ├── account_already_exists_subject.txt
    │   │   ├── base_message.txt
    │   │   ├── email_confirmation_message.txt
    │   │   ├── email_confirmation_signup_message.txt
    │   │   ├── email_confirmation_signup_subject.txt
    │   │   ├── email_confirmation_subject.txt
    │   │   ├── password_reset_key_message.txt
    │   │   ├── password_reset_key_subject.txt
    │   │   ├── unknown_account_message.txt
    │   │   └── unknown_account_subject.txt
    │   ├── messages/
    │   │   ├── cannot_delete_primary_email.txt
    │   │   ├── email_confirmation_failed.txt
    │   │   ├── email_confirmation_sent.txt
    │   │   ├── email_confirmed.txt
    │   │   ├── email_deleted.txt
    │   │   ├── logged_in.txt
    │   │   ├── logged_out.txt
    │   │   ├── password_changed.txt
    │   │   ├── password_set.txt
    │   │   ├── primary_email_set.txt
    │   │   └── unverified_primary_email.txt
    │   └── snippets/
    │       ├── already_logged_in.html
    │       └── warn_no_email.html
    ├── pages/
    │   ├── archive/
    │   │   └── login.html
    │   ├── bulk_response/
    │   │   └── bulk_response.html
    │   ├── chat/
    │   │   ├── chat_selection.html
    │   │   └── chat.html
    │   ├── create_avatar/
    │   │   └── create_avatar.html
    │   ├── experts/
    │   │   └── experts.html
    │   ├── home/
    │   │   ├── admin.html
    │   │   ├── home.html
    │   │   └── landing.html
    │   ├── interview/
    │   │   ├── interivew_Jan7end_save.html
    │   │   ├── interview.html
    │   │   ├── interview_Feb19_save.html
    │   │   ├── interview_Jan7_save.html
    │   │   ├── interview_OLD.html
    │   │   ├── interview_base.html
    │   │   └── interview_modals.html
    │   ├── summary/
    │   │   └── summary.html
    │   └── transcript/
    │       └── transcript.html
    └── socialaccount/
        ├── authentication_error.html
        ├── base.html
        ├── connections.html
        ├── login.html
        ├── login_cancelled.html
        ├── signup.html
        ├── messages/
        │   ├── account_connected.txt
        │   ├── account_connected_other.txt
        │   ├── account_connected_updated.txt
        │   └── account_disconnected.txt
        └── snippets/
            ├── login_extra.html
            └── provider_list.html
```

This structure separates concerns by grouping similar functionalities together:
- **gabm_infra:** Core infrastructure, project settings, and URL configurations.
- **interviewer_agent:** Logic for interview scripting, agent modules (transcription, vocalization), and GPT prompt templates.
- **pages:** Django app containing models, views, forms, pipelines, and migrations for the interview process, simulation interaction and participant management.
- **sim_brain:** Logic for the simulations, including different "brain" implementations, and their related database models.
- **templates:** HTML templates for various parts of the application, including account management, interview interfaces, simulation interactive interfaces and administrative summaries.

---

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/gabm_interviewer_platform.git
   cd gabm_interviewer_platform
   ```

2. **Set Up a Virtual Environment**

   It is recommended to use a virtual environment to manage dependencies.

   ```bash
   python -m venv venv
   source venv/Scripts/activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**

   Set up your database:

   ```bash
   python manage.py migrate
   ```

5. **Collect Static Files (if applicable)**

   ```bash
   python manage.py collectstatic
   ```

---

## Usage

1. **Create the Database**
   If you need to re-initialise the database, delete `db.sqlite3` in the project root and then run:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Creating an Admin Account**

   ```bash
   python manage.py createsuperuser
   ```
   Access the application admin page at [http://localhost:8000/admin](http://localhost:8000/admin)

3. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

   Access the application at [http://localhost:8000](http://localhost:8000).

4. **Managing Interviews**

   - Configure interview settings via the Django admin interface or through dedicated settings within the `pages` app.
   - Update or customize interview scripts located in `interviewer_agent/interview_script/new_avp_full_v1/` as needed.
   - Utilize the agent modules in `interviewer_agent/agent_modules/` for transcription and vocalization functionalities during interviews.

5. **Loading Interview Data**

   - As an administrator, access [http://localhost:8000/summary](http://localhost:8000/summary) to view the participant list.
   - From this page, you can load interview data.

6. **Interacting with Simulations**

   - As an administrator, access [http://localhost:8000/chat](http://localhost:8000/chat) to select a simulation to chat with or access [http://localhost:8000/bulk-response](http://localhost:8000/bulk-response) to query the simulation with a bulk list of questions.

7. **Working with Templates**

   Customize the look and feel of the platform by editing the HTML templates located in the `templates/` directory.

---

## Configuration

- **Settings:** The core settings are managed in `gabm_infra/settings/base.py`. Adjust database configurations, allowed hosts, and other Django settings here.
- **Deployment Files:** The repository includes:
  - **Procfile**: For Heroku deployment.
  - **Aptfile**: To specify additional system-level dependencies.
  - **runtime.txt**: To define the Python runtime version.
  - **app.yaml**: Configuration for Google App Engine deployment.- **compose.yml**: Docker Compose file for multi-container Docker applications.
  - **Dockerfile**: Dockerfile for building the application image.
  - **entrypoint.sh**: Entrypoint script for Docker containers.
- **.env:** The necessary environment variables to run this project includes:
  - **SECRET_KEY**: Django server secret key.
  - **ALLOWED_HOSTS**: A comma-separated list of valid hostnames for the Django application.
  - **OPENAI_API_KEY**: The OpenAI API key for GPT-based functionalities.
  - **OPENAI_API_KEY_OWNER**: The owner of the OpenAI API key.
  - **GOOGLE_CRED_PATH**: The path to your Google Cloud service account key JSON file for Google Cloud services (e.g., transcription/vocalization).
  - **OPENAI_API_KEY_OWNER**: The owner of the OpenAI API key.
  - **DATABASE_ENGINE**: The database engine for the database.
  - **DATABASE_NAME**: The database name.
  - **DATABASE_USERNAME**: The username to access the database.
  - **DATABASE_PASSWORD**: The password to access the databse.
  - **DATABASE_HOST**: The database host.
  - **DATABASE_PORT**: The database port.
  - **ADMIN_USERNAME**: The admin username used to access the admin dashboard.
  - **ADMIN_EMAIL**: The admin email used to access the admin dashboard.
  - **ADMIN_PASSWORD**: The admin password used to access the admin dashboard.
  - **CONTACT_EMAIL**: The default email that participant's will have access to contact. This can be changed at runtime.
  - **CONSENT_FORM_LINK**: The default link to the consent form that participant's will read. This can be changed at runtime.
  - **SURVEY_1_LINK**: The default link to the first survey that participant's will have to complete. This can be changed at runtime.
  - **SURVEY_1_SECRET**: The default password for the first survey that participants will provide to prove that they have completed the survey. This can be changed at runtime.
  - **SURVEY_2_LINK**: The default link to the second survey that participant's will have to complete. This can be changed at runtime.
  - **SURVEY_2_SECRET**: The default password for the second survey that participants will provide to prove that they have completed the survey. This can be changed at runtime.

---

## Contributing

Contributions are welcome! If you would like to contribute to the project, please:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes with clear descriptions.
4. Submit a pull request detailing your changes.

Please follow the existing code style and include tests for any new features or bug fixes.

---

## License

This project is licensed under the [MIT License](LICENSE).
