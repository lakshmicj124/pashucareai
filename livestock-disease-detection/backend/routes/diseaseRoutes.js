const express = require('express');
const router = express.Router();
const diseaseController = require('../controllers/diseaseController');
const jwt = require('jsonwebtoken');

const authMiddleware = (req, res, next) => {
  const token = req.header('Authorization')?.replace('Bearer ', '');
  if (!token) return res.status(401).json({ message: 'No token, authorization denied' });
  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = decoded;
    next();
  } catch (err) {
    res.status(401).json({ message: 'Token is not valid' });
  }
};

const adminMiddleware = (req, res, next) => {
  if (req.user && req.user.role === 'admin') {
    next();
  } else {
    res.status(403).json({ message: 'Forbidden: Admin access only' });
  }
};

router.get('/', authMiddleware, diseaseController.getDiseases);
router.get('/details', authMiddleware, diseaseController.getDiseaseDetailsByName);

// Admin Routes
router.post('/', authMiddleware, adminMiddleware, diseaseController.createDisease);
router.put('/:id', authMiddleware, adminMiddleware, diseaseController.updateDisease);
router.delete('/:id', authMiddleware, adminMiddleware, diseaseController.deleteDisease);

module.exports = router;
