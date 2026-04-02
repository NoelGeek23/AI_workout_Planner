# AI_workout_Planner

## Overview
This application generates custom workout plans based on user inputs such as fitness level, age, and available workout time using AI.

## Features
- User-friendly interface for inputting personal data.
- Secure API for handling user data.
- AI-driven workout plan generation.
- Logging and monitoring for performance and security.

## Getting Started
1. Clone the repository.
2. Install dependencies.
3. Run the application.

## API Specifications
- **POST /api/workout-plan**: Generate a custom workout plan.
  - **Request Body**:
    - `fitness_level`: String (e.g., 'beginner', 'intermediate', 'advanced')
    - `age`: Integer
    - `available_time`: Integer (in minutes)
  - **Response**:
    - `workout_plan`: Object containing the generated workout routine.

## Security
User data is encrypted and securely stored to ensure privacy.