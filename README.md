# UltimateFitnessTracker
SEI29-Project4

### Elevator Pitch
Fitness based UI website that allow users to create and track their fitness goal with the excitement of getting their summer body goal once this whole pandemic dies down

### User Stories
User looking for better way to create a workout plan that siuts their daily lifestyle and track their progress, comes to website and creates account and starts planning out their weekly workout schedule and updating their workout logs.

### Wireframes
[Link to wireframes](https://docs.google.com/document/d/1-d6pXOz45mgQm5xr3QPk_3H3vUi4wcxALnU_YEToGos/edit?usp=sharing)
* Wireframe for Dashboard (main page)
* Wireframe for user profile
* Wireframe for login page
* Wireframe for signup page
* Wireframe for the workouk page
* Wireframe for the exercise page

### Proposed Architecture
Backend with Flask - App has minimal routing, and preformance is held on single plage (meaning my dashboard page), so use and scabality won’t be an issue.

Authentication - using oAuth (in Python).

Frontend with HTML/CSS/Boostrap4 - No new technologies being use. MVP is going to be a clean, introductory site with full functionality of wger REST API. Further design will be implemented based on feedback from UX designer.

Wger REST API (Python Interface) - Second new technology allowing me to integrate list of workouts into my app.

### MVP (working list for in class):
Have a full CRUD app for a user to login, authenticate, and create accounts.
Be able to create and post your workouk (any other feature or related activies, etc.) will be post MVP.
link description here

### Routes
Action | Method | Function Name | Path |
|------|--------|---------------|------|
|Index | GET |  | index()|  /index |
|Profile | GET | profile()|/profile |
|Auth Login | GET, POST |login()|/login|
|Auth signup | GET, POST |signup()|/sigup|
|Create*|POST | workouts() | /workout|
|update profile | PUT | edit_profile()|/profile/edit |
|Update workout | PUT | edit_workout() |workout/<int:id> |
|Delete| DELETE |delete_workout() |workout/<int:id> |
