require('dotenv').config();
const express = require('express');
const cors = require('cors');

const app = express();
const port = process.env.PORT || 5000;

// Middleware
app.use(cors());
app.use(express.json());
app.use('/uploads', express.static('uploads'));

// Routes
const authRoutes = require('./routes/authRoutes');
const uploadRoutes = require('./routes/uploadRoutes');
const historyRoutes = require('./routes/historyRoutes');
const diseaseRoutes = require('./routes/diseaseRoutes');
const userRoutes = require('./routes/userRoutes');
app.use('/api/auth', authRoutes);
app.use('/api/upload', uploadRoutes);
app.use('/api/history', historyRoutes);
app.use('/api/disease', diseaseRoutes);
app.use('/api/users', userRoutes);

// Basic Route
app.get('/', (req, res) => {
  res.send('Cow Disease API is running');
});

// Start Server
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
