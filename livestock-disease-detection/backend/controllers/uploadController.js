const pool = require('../db');
const nodemailer = require('nodemailer');

// Mock AI function for disease detection
const detectDisease = (imageUrl) => {
  return new Promise((resolve) => {
    setTimeout(() => {
      // Return mock data
      resolve({
        disease: 'Foot and Mouth Disease (Mock)',
        confidence: 92.5
      });
    }, 2000); // simulate delay
  });
};

// Email sender function
const sendDiseaseNotification = async (userEmail, userName, diseaseName, confidence) => {
  if (!process.env.EMAIL_USER || !process.env.EMAIL_PASS) {
    console.log(`[Email Mock Logger] To: ${userEmail}`);
    console.log(`Subject: Alert: Disease Detected in Livestock`);
    console.log(`Body: Hello ${userName}, our AI has detected ${diseaseName} (Confidence: ${confidence}%) in your livestock upload. Please check the dashboard for details.`);
    return;
  }

  try {
    const transporter = nodemailer.createTransport({
      service: 'gmail',
      auth: {
        user: process.env.EMAIL_USER,
        pass: process.env.EMAIL_PASS,
      },
    });

    const mailOptions = {
      from: process.env.EMAIL_USER,
      to: userEmail,
      subject: '🚨 Alert: Disease Detected in Livestock',
      html: `
        <div style="font-family: sans-serif; padding: 20px; color: #333;">
          <h2>Livestock Disease Detection Alert</h2>
          <p>Hello <strong>${userName}</strong>,</p>
          <p>Our AI system has completed analyzing your uploaded image and detected a potential health issue:</p>
          <div style="background-color: #f8d7da; border: 1px solid #f5c6cb; padding: 15px; border-radius: 5px; margin: 20px 0;">
            <p style="margin: 0; font-size: 18px; color: #721c24;"><strong>Detected Disease:</strong> ${diseaseName}</p>
            <p style="margin: 5px 0 0 0; font-size: 16px; color: #721c24;"><strong>Confidence Score:</strong> ${confidence}%</p>
          </div>
          <p>Please log in to your dashboard to review full description details and recommended treatments.</p>
          <hr style="border: 0; border-top: 1px solid #eee; margin: 20px 0;" />
          <p style="font-size: 12px; color: #777;">This is an automated alert from the Livestock AI Health Assistant platform.</p>
        </div>
      `,
    };

    await transporter.sendMail(mailOptions);
    console.log(`Disease notification email sent successfully to ${userEmail}`);
  } catch (error) {
    console.error('Failed to send disease notification email:', error.message);
  }
};

exports.uploadImage = async (req, res) => {
  try {
    if (!req.file) {
      return res.status(400).json({ message: 'No image uploaded' });
    }

    const imageUrl = `/uploads/${req.file.filename}`;

    // 1. Process image with Mock AI
    const result = await detectDisease(imageUrl);

    // 2. Save history in DB
    const newHistory = await pool.query(
      'INSERT INTO detection_history (user_id, image_url, detected_disease, confidence_score) VALUES ($1, $2, $3, $4) RETURNING *',
      [req.user.id, imageUrl, result.disease, result.confidence]
    );

    // 3. Fetch user details to get email & name
    const userRes = await pool.query('SELECT name, email FROM users WHERE id = $1', [req.user.id]);
    if (userRes.rows.length > 0) {
      const { email, name } = userRes.rows[0];
      // Run async in background so response is not delayed
      sendDiseaseNotification(email, name, result.disease, result.confidence);
    }

    res.json({
      message: 'Image analyzed successfully',
      history: newHistory.rows[0],
      detection: result
    });
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Server error during upload/analysis' });
  }
};

