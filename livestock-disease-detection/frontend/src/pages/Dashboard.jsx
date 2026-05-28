import { useEffect, useState, useContext } from 'react';
import { AuthContext } from '../context/AuthContext';
import axios from 'axios';
import { LayoutDashboard, LogOut, Upload, History } from 'lucide-react';
import { Link, useNavigate } from 'react-router-dom';

export default function Dashboard() {
  const { user, logout } = useContext(AuthContext);
  const [history, setHistory] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchHistory = async () => {
      try {
        const token = localStorage.getItem('token');
        const res = await axios.get('http://localhost:5000/api/history', {
          headers: { Authorization: `Bearer ${token}` }
        });
        setHistory(res.data);
      } catch (err) {
        console.error(err);
      }
    };
    fetchHistory();
  }, []);

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <div className="min-h-screen bg-gray-100 flex">
      {/* Sidebar */}
      <div className="w-64 bg-white shadow-md flex flex-col justify-between">
        <div className="p-6">
          <h2 className="text-xl font-bold text-gray-800 flex items-center gap-2">
            <LayoutDashboard className="text-blue-600" />
            Livestock AI
          </h2>
          <nav className="mt-8 space-y-2">
            <Link to="/dashboard" className="flex items-center gap-3 px-4 py-2 bg-blue-50 text-blue-700 font-semibold rounded-md">
              <LayoutDashboard size={20} />
              Dashboard
            </Link>
            <Link to="/upload" className="flex items-center gap-3 px-4 py-2 text-gray-600 hover:bg-gray-50 rounded-md">
              <Upload size={20} />
              Detect Disease
            </Link>
          </nav>
        </div>
        <div className="p-6 border-t">
          <div className="flex items-center gap-3 mb-4">
            <div className="h-10 w-10 bg-blue-100 rounded-full flex items-center justify-center font-bold text-blue-700">
              {user?.name?.[0]?.toUpperCase() || 'U'}
            </div>
            <div>
              <p className="text-sm font-semibold text-gray-800">{user?.name}</p>
              <p className="text-xs text-gray-500 capitalize">{user?.role}</p>
            </div>
          </div>
          <button
            onClick={handleLogout}
            className="w-full flex items-center justify-center gap-2 px-4 py-2 border border-gray-300 rounded-md text-sm text-gray-600 hover:bg-gray-50 transition-colors"
          >
            <LogOut size={16} />
            Logout
          </button>
        </div>
      </div>

      {/* Main Content */}
      <div className="flex-1 p-10">
        <header className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900">Welcome Back, {user?.name}!</h1>
          <p className="text-gray-600 mt-1">Here is the latest health status and detection history of your livestock.</p>
        </header>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
          <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-150">
            <h3 className="text-sm font-semibold text-gray-500 uppercase tracking-wider">Total Scans</h3>
            <p className="text-3xl font-extrabold text-gray-900 mt-2">{history.length}</p>
          </div>
          <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-150">
            <h3 className="text-sm font-semibold text-gray-500 uppercase tracking-wider">Last Detection</h3>
            <p className="text-xl font-bold text-gray-900 mt-2 truncate">
              {history[0]?.detected_disease || 'No scans yet'}
            </p>
          </div>
          <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-150 flex items-center justify-center">
            <Link to="/upload" className="w-full flex items-center justify-center gap-2 px-6 py-3 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 transition-colors">
              <Upload size={20} />
              New Scan
            </Link>
          </div>
        </div>

        {/* History Table */}
        <div className="bg-white rounded-xl shadow-sm border border-gray-150 overflow-hidden">
          <div className="px-6 py-4 border-b border-gray-150 flex justify-between items-center">
            <h2 className="font-bold text-gray-800 flex items-center gap-2">
              <History size={18} className="text-gray-500" />
              Recent Scans
            </h2>
          </div>
          {history.length === 0 ? (
            <div className="p-8 text-center text-gray-500">
              No scans performed yet. Click "New Scan" to check your livestock.
            </div>
          ) : (
            <table className="min-w-full divide-y divide-gray-200">
              <thead className="bg-gray-50">
                <tr>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Image</th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Detected Disease</th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Confidence</th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Date</th>
                </tr>
              </thead>
              <tbody className="bg-white divide-y divide-gray-200">
                {history.map((scan) => (
                  <tr key={scan.id}>
                    <td className="px-6 py-4 whitespace-nowrap">
                      <img src={`http://localhost:5000${scan.image_url}`} alt="Scan" className="w-12 h-12 object-cover rounded-md border" />
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap font-medium text-gray-900">{scan.detected_disease}</td>
                    <td className="px-6 py-4 whitespace-nowrap">
                      <span className="px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800">
                        {scan.confidence_score}%
                      </span>
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                      {new Date(scan.created_at).toLocaleDateString()}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </div>
      </div>
    </div>
  );
}
