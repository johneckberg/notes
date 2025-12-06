# project recall notes

- Get ubuntu server up on grandmas laptop
- fix chatgpt integration for automatic generation (fix edge cases)
- UI changes:
  - ben says nothing major that he recalls
  - look at it and see what you think
- backend is postgres: should be good
  - just has the flashcards using sql
- flashcards are not persistent (sometimes?)
  - looking at docker compose, references volume, but using docker volumes locally which "isn't the right way to do this"

- ben plans on using kustomize & kind k8 clusters instead of docker compose moving forward

## flashcards are organized by tags, find a better feature to organize the flashcards

## tags should be semantic 

## need bens .env file for the api key

## API Endpoints

- `GET /flashcards` - Get all flashcards
- `GET /flashcards/{id}` - Get specific flashcard
- `GET /flashcards/random/one` - Get random flashcard
- `POST /flashcards` - Create new flashcard
- `PUT /flashcards/{id}` - Update flashcard
- `DELETE /flashcards/{id}` - Delete flashcard

## Development

### Backend Development
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend Development
```bash
cd frontend
npm install
npm run dev
```