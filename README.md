# UNIT-PROJECT-2

# Mirah

**Mirah** is a smart Django-based system for tracking, documenting, and managing livestock herds.  
The word "Mirah" (مراح) comes from Arabic and refers to the traditional resting place for animals — a symbol of routine, care, and herd management.

## Features
- Manage animal types and breeds
- Add, view, and track animals
- Record and monitor animal weight and ideal growth
- Add and track vaccination records
- Custom vaccination logic (alerts for missing vaccines based on age, gender, and breed)
- Upload and store media files (e.g., animal images, vaccination docs)
- Responsive design using Tailwind CSS
- Media storage with ImageKit

## Files
- [User Stories](Files/Mirah_UserStories.pdf)
- [UML Diagram](Files/Mirah_UMLDiagram.png)
- [Wireframes](Files/Mirah_Wireframes.pdf)

## Technologies & Libraries Used
### Core Technologies
- **Python** — Programming language used to build the backend logic.
- **Django** — Web framework used to structure the backend and implement business logic.
- **HTML / Tailwind CSS** — Used to design and style responsive, modern user interfaces.

### Third-Party Libraries
- **[django-tables2](https://pypi.org/project/django-tables2/)**  
  Used to render dynamic, paginated tables for displaying records like animals, breeds, and vaccines.

- **[django-filter](https://pypi.org/project/django-filter/)**  
  Enables powerful filtering and search functionality for tables, allowing users to filter data easily.

- **[django-crispy-forms](https://pypi.org/project/django-crispy-forms/)**  
  Helps render Django forms with clean HTML and styling, especially with Tailwind CSS integration.

- **[python-dateutil](https://pypi.org/project/python-dateutil/)**  
  Used to calculate animal age (in years, months, and days) via `relativedelta` for tracking growth and vaccination eligibility.

- **[python-dotenv](https://pypi.org/project/python-dotenv/)**  
  Used to manage environment variables and keep sensitive data like API keys and secret settings outside the source code.

- **[ImageKit](https://imagekit.io/)**  
  A cloud-based CDN and storage provider used to serve images and videos efficiently (e.g., animal photos, intro video).