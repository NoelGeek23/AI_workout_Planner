const { generateWorkoutPlan } = require('../services/workoutService');

describe('Workout Service', () => {
    test('should generate a workout plan based on user inputs', async () => {
        const plan = await generateWorkoutPlan('beginner', 25, 30);
        expect(plan).toHaveProperty('exercises');
        expect(plan.total_time).toBe(30);
    });
});