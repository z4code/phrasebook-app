# Phrasebook App

The **Phrasebook App** is a Django-based web application designed to store, manage, and display phrases in different languages. Users can browse through various categories of phrases, view translations, and even play audio recordings for the correct pronunciation of each phrase.

## Features

- **Language and Category Management**: Organize phrases by language and category.
- **Phrase Translation**: Each phrase comes with a translation in another language.
- **Pronunciation Guide**: Audio and text-based pronunciation available for phrases.
- **Favorite Phrases**: Users can mark phrases as favorites for quick access.
- **Bootstrap 5**: Styled with the modern, responsive framework.
- **Google Fonts**: SUSE font for a clean and professional look.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/z4code/phrasebook-app.git
    cd phrasebook-app
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

6. **Access the app**:
    Open your browser and visit `http://127.0.0.1:8000`.

## Technologies Used

- **Django**: Backend framework for building the app.
- **Bootstrap 5**: For responsive, mobile-first design.
- **Google Fonts (SUSE)**: To enhance the typography of the site.
- **Slugify**: Automatically generates slugs for URL-friendly paths.
- **FileField**: For uploading audio files of phrase pronunciations.

## Models

1. **Language**:
    - `name`: Name of the language.
    - `slug`: Auto-generated URL slug.

2. **Category**:
    - `name`: Name of the category (e.g., greetings, travel).
    - `slug`: Auto-generated URL slug.
    - `icon`: Optional icon representing the category.
    - `language`: Foreign key linking to the `Language` model.

3. **Phrase**:
    - `text`: The original phrase.
    - `translation`: Translation of the phrase.
    - `category`: Foreign key linking to the `Category` model.
    - `language`: Foreign key linking to the `Language` model.
    - `audio`: Optional audio file for pronunciation.
    - `pronunciation`: Text-based pronunciation guide.
    - `favorite`: Boolean to mark the phrase as a favorite.
    - `added_on`: Timestamp for when the phrase was added.

## Views

- **Home**: Displays all categories available.
- **View Category**: Displays all phrases belonging to a specific category, along with their translations and other details.

## Credits

- **Author**: Diyorbek Qodirboyev
- **Icon**: <a href="https://www.flaticon.com/free-icons/book" title="book icons">Book icons created by Smashicons - Flaticon</a>

## License

This project is open-source and available under the [MIT License](LICENSE).

