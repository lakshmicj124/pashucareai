const pool = require('../db');

exports.getDiseases = async (req, res) => {
  try {
    const result = await pool.query('SELECT * FROM diseases');
    res.json(result.rows);
  } catch (error) {
    console.error(error.message);
    res.status(500).json({ message: 'Server Error' });
  }
};

exports.getDiseaseDetailsByName = async (req, res) => {
  const { name } = req.query;
  try {
    const result = await pool.query('SELECT * FROM diseases WHERE name ILIKE $1', [`%${name}%`]);
    if (result.rows.length === 0) {
      return res.status(404).json({ message: 'Disease details not found' });
    }
    res.json(result.rows[0]);
  } catch (error) {
    console.error(error.message);
    res.status(500).json({ message: 'Server Error' });
  }
};

// Admin CRUD
exports.createDisease = async (req, res) => {
  const { name, animal_type, description, treatment } = req.body;
  try {
    const result = await pool.query(
      'INSERT INTO diseases (name, animal_type, description, treatment) VALUES ($1, $2, $3, $4) RETURNING *',
      [name, animal_type, description, treatment]
    );
    res.status(201).json(result.rows[0]);
  } catch (error) {
    console.error(error.message);
    res.status(500).json({ message: 'Server Error' });
  }
};

exports.updateDisease = async (req, res) => {
  const { id } = req.params;
  const { name, animal_type, description, treatment } = req.body;
  try {
    const result = await pool.query(
      'UPDATE diseases SET name = $1, animal_type = $2, description = $3, treatment = $4 WHERE id = $5 RETURNING *',
      [name, animal_type, description, treatment, id]
    );
    res.json(result.rows[0]);
  } catch (error) {
    console.error(error.message);
    res.status(500).json({ message: 'Server Error' });
  }
};

exports.deleteDisease = async (req, res) => {
  const { id } = req.params;
  try {
    await pool.query('DELETE FROM diseases WHERE id = $1', [id]);
    res.json({ message: 'Disease deleted successfully' });
  } catch (error) {
    console.error(error.message);
    res.status(500).json({ message: 'Server Error' });
  }
};
