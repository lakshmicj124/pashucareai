import { useState, useContext } from 'react';
import { AuthContext } from '../context/AuthContext';
import axios from 'axios';
import { Upload, ArrowLeft, Loader2, CheckCircle2 } from 'lucide-react';
import { Link, useNavigate } from 'react-router-dom';

export default function UploadImage() {
  const { user } = useContext(AuthContext);
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [diseaseDetails, setDiseaseDetails] = useState(null);
  const navigate = useNavigate();

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile) {
      setFile(selectedFile);
      setPreview(URL.createObjectURL(selectedFile));
      setResult(null);
      setDiseaseDetails(null);
    }
  };

  const handleUpload = async (e) => {
    e.preventDefault();
    if (!file) return;

    setLoading(true);
    const formData = new FormData();
    formData.append('image', file);

    try {
      const token = localStorage.getItem('token');
      const res = await axios.post('http://localhost:5000/api/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
          Authorization: `Bearer ${token}`
        }
      });
      setResult(res.data.detection);

      // Fetch disease details
      try {
        const detailsRes = await axios.get(`http://localhost:5000/api/disease/details?name=${res.data.detection.disease}`, {
          headers: { Authorization: `Bearer ${token}` }
        });
        setDiseaseDetails(detailsRes.data);
      } catch (detailsErr) {
        console.warn('Could not load specific disease details: ', detailsErr.message);
      }
    } catch (err) {
      console.error(err);
      alert('Error analyzing image');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 py-10 px-4 sm:px-6 lg:px-8">
      <div className="max-w-2xl mx-auto">
        <Link to="/dashboard" className="inline-flex items-center gap-2 text-sm text-gray-500 hover:text-gray-800 mb-6">
          <ArrowLeft size={16} />
          Back to Dashboard
        </Link>

        <div className="bg-white rounded-xl shadow-lg border border-gray-100 p-8">
          <h2 className="text-2xl font-bold text-gray-900 mb-2">AI Livestock Disease Detection</h2>
          <p className="text-gray-500 mb-8">Upload a clear photo of the cow, goat, or sheep's affected area to run the diagnostic scan.</p>

          <form onSubmit={handleUpload} className="space-y-6">
            <div className="border-2 border-dashed border-gray-300 rounded-lg p-6 flex flex-col items-center justify-center hover:border-blue-500 transition-colors relative cursor-pointer">
              <input
                type="file"
                accept="image/*"
                onChange={handleFileChange}
                className="absolute inset-0 w-full h-full opacity-0 cursor-pointer"
              />
              {preview ? (
                <img src={preview} alt="Preview" className="max-h-64 rounded-md object-cover" />
              ) : (
                <div className="text-center">
                  <Upload className="mx-auto h-12 w-12 text-gray-400 mb-3" />
                  <p className="text-sm text-gray-600 font-medium">Click or drag image here to upload</p>
                  <p className="text-xs text-gray-400 mt-1">PNG, JPG, JPEG up to 10MB</p>
                </div>
              )}
            </div>

            {file && !result && (
              <button
                type="submit"
                disabled={loading}
                className="w-full flex items-center justify-center gap-2 py-3 bg-blue-600 hover:bg-blue-700 text-white font-semibold rounded-lg disabled:bg-blue-300 transition-colors"
              >
                {loading ? (
                  <>
                    <Loader2 className="animate-spin" size={20} />
                    Analyzing Image...
                  </>
                ) : (
                  'Start AI Analysis'
                )}
              </button>
            )}
          </form>

          {result && (
            <div className="mt-8 p-6 bg-green-50 border border-green-150 rounded-xl">
              <h3 className="text-lg font-bold text-green-900 flex items-center gap-2 mb-4">
                <CheckCircle2 className="text-green-600" />
                Diagnostic Report Complete
              </h3>
              <div className="space-y-4">
                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <span className="text-xs font-bold text-green-700 uppercase tracking-wider">Detected Condition</span>
                    <p className="text-lg font-extrabold text-gray-900 mt-0.5">{result.disease}</p>
                  </div>
                  <div>
                    <span className="text-xs font-bold text-green-700 uppercase tracking-wider">Confidence Score</span>
                    <p className="text-lg font-extrabold text-gray-900 mt-0.5">{result.confidence}%</p>
                  </div>
                </div>

                {diseaseDetails && (
                  <div className="border-t border-green-200 pt-4 space-y-3">
                    <div>
                      <span className="text-xs font-bold text-green-700 uppercase tracking-wider">Description</span>
                      <p className="text-sm text-gray-700 mt-1 leading-relaxed">{diseaseDetails.description}</p>
                    </div>
                    <div>
                      <span className="text-xs font-bold text-green-700 uppercase tracking-wider">Recommended Treatment</span>
                      <p className="text-sm text-gray-700 mt-1 leading-relaxed">{diseaseDetails.treatment}</p>
                    </div>
                  </div>
                )}

                <div className="pt-4">
                  <Link to="/dashboard" className="px-4 py-2 bg-green-600 text-white rounded-lg font-semibold hover:bg-green-700 transition-colors inline-block">
                    Save and Exit
                  </Link>
                </div>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
