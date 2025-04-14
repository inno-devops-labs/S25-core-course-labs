const express = require('express');
const router = express.Router();
const timeController = require('../controllers/timeController');

// Endpoint to render Moscow time
router.get('/', timeController.getMoscowTime);

module.exports = router;