const pool = require('../db');

exports.getHistory = async (req, res) => {
  try {
    const history = await pool.query(
      'SELECT * FROM detection_history WHERE user_id = $1 ORDER BY created_at DESC',
      [req.user.id]
    );
    res.json(history.rows);
  } catch (error) {
    console.error(error.message);
    res.status(500).json({ message: 'Server Error' });
  }
};
