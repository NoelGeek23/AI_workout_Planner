const { generateAIWorkoutPlan } = require('./aiService');

async function generateWorkoutPlan(fitness_level, age, available_time) {
    // Call AI service to generate a workout plan
    const workoutPlan = await generateAIWorkoutPlan(fitness_level, age, available_time);
    return workoutPlan;
}

module.exports = { generateWorkoutPlan };