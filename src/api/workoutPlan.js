const express = require('express');
const router = express.Router();
const { generateWorkoutPlan } = require('../services/workoutService');

router.post('/workout-plan', async (req, res) => {
    const { fitness_level, age, available_time } = req.body;
    try {
        const workoutPlan = await generateWorkoutPlan(fitness_level, age, available_time);
        res.status(200).json({ workout_plan: workoutPlan });
    } catch (error) {
        res.status(500).json({ error: 'Failed to generate workout plan' });
    }
});

module.exports = router;