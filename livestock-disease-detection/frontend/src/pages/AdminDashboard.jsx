import { useEffect, useState, useContext } from 'react';
import { AuthContext } from '../context/AuthContext';
import axios from 'axios';
import { LayoutDashboard, LogOut, Users, BookOpen, Plus, Edit2, Trash2 } from 'lucide-react';
import { useNavigate } from 'react-router-dom';

export default function AdminDashboard() {
  const { user, logout } = useContext(AuthContext);
  const [users, setUsers] = useState([]);
  const [diseases, setDiseases] = useState([]);
  const [viewMode, setViewMode] = useState('users'); // 'users' or 'diseases'
  
  // Form state for add/edit disease
  const [editingDisease, setEditingDisease] = useState(null);
  const [showForm, setShowForm] = useState(false);
  const [name, setName] = useState('');
  const [animalType, setAnimalType] = useState('cow');
  const [description, setDescription] = useState('');
  const [treatment, setTreatment] = useState('');

  const navigate = useNavigate();
  const token = localStorage.getItem('token');

  const fetchData = async () => {
    try {
      const usersRes = await axios.get('http://localhost:5000/api/users', {
        headers: { Authorization: `Bearer ${token}` }
      });
      setUsers(usersRes.data);

      const diseasesRes = await axios.get('http://localhost:5000/api/disease', {
        headers: { Authorization: `Bearer ${token}` }
      });
      setDiseases(diseasesRes.data);
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  const handleSaveDisease = async (e) => {
    e.preventDefault();
    try {
      if (editingDisease) {
        // Update
        await axios.put(`http://localhost:5000/api/disease/${editingDisease.id}`, 
          { name, animal_type: animalType, description, treatment },
          { headers: { Authorization: `Bearer ${token}` } }
        );
      } else {
        // Create
        await axios.post('http://localhost:5000/api/disease', 
          { name, animal_type: animalType, description, treatment },
          { headers: { Authorization: `Bearer ${token}` } }
        );
      }
      setShowForm(false);
      setEditingDisease(null);
      setName('');
      setDescription('');
      setTreatment('');
      fetchData();
    } catch (err) {
      console.error(err);
      alert('Error saving disease');
    }
  };

  const handleEditClick = (disease) => {
    setEditingDisease(disease);
    setName(disease.name);
    setAnimalType(disease.animal_type);
    setDescription(disease.description);
    setTreatment(disease.treatment);
    setShowForm(true);
  };

  const handleDeleteDisease = async (id) => {
    if (!confirm('Are you sure you want to delete this disease details?')) return;
    try {
      await axios.delete(`http://localhost:5000/api/disease/${id}`, {
        headers: { Authorization: `Bearer ${token}` }
      });
      fetchData();
    } catch (err) {
      console.error(err);
      alert('Error deleting disease');
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex">
      {/* Sidebar */}
      <div className="w-64 bg-white shadow-md flex flex-col justify-between">
        <div className="p-6">
          <h2 className="text-xl font-bold text-gray-800 flex items-center gap-2">
            <LayoutDashboard className="text-red-600" />
            Admin Panel
          </h2>
          <nav className="mt-8 space-y-2">
            <button
              onClick={() => setViewMode('users')}
              className={`w-full flex items-center gap-3 px-4 py-2 rounded-md text-left font-semibold ${
                viewMode === 'users' ? 'bg-red-50 text-red-700' : 'text-gray-600 hover:bg-gray-50'
              }`}
            >
              <Users size={20} />
              View Users
            </button>
            <button
              onClick={() => setViewMode('diseases')}
              className={`w-full flex items-center gap-3 px-4 py-2 rounded-md text-left font-semibold ${
                viewMode === 'diseases' ? 'bg-red-50 text-red-700' : 'text-gray-600 hover:bg-gray-50'
              }`}
            >
              <BookOpen size={20} />
              Manage Diseases
            </button>
          </nav>
        </div>
        <div className="p-6 border-t">
          <div className="flex items-center gap-3 mb-4">
            <div className="h-10 w-10 bg-red-100 rounded-full flex items-center justify-center font-bold text-red-700">
              A
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
        <header className="flex justify-between items-center mb-8">
          <div>
            <h1 className="text-3xl font-bold text-gray-900">
              {viewMode === 'users' ? 'Registered Users' : 'Disease Database Management'}
            </h1>
            <p className="text-gray-600 mt-1">
              {viewMode === 'users' 
                ? 'Review user accounts and system registration activity.' 
                : 'Add, update, or remove disease catalog information.'}
            </p>
          </div>
          {viewMode === 'diseases' && (
            <button
              onClick={() => {
                setEditingDisease(null);
                setName('');
                setDescription('');
                setTreatment('');
                setShowForm(true);
              }}
              className="flex items-center gap-2 px-4 py-2 bg-red-600 hover:bg-red-700 text-white rounded-lg font-semibold transition-colors"
            >
              <Plus size={18} />
              Add Disease
            </button>
          )}
        </header>

        {showForm && (
          <div className="mb-8 p-6 bg-white rounded-xl shadow-sm border border-gray-200">
            <h3 className="text-lg font-bold text-gray-800 mb-4">
              {editingDisease ? 'Edit Disease' : 'Add New Disease'}
            </h3>
            <form onSubmit={handleSaveDisease} className="space-y-4">
              <div className="grid grid-cols-2 gap-4">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">Disease Name</label>
                  <input
                    type="text"
                    required
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    className="w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-red-500"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">Animal Type</label>
                  <select
                    value={animalType}
                    onChange={(e) => setAnimalType(e.target.value)}
                    className="w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-red-500"
                  >
                    <option value="cow">Cow</option>
                    <option value="goat">Goat</option>
                    <option value="sheep">Sheep</option>
                  </select>
                </div>
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">Description</label>
                <textarea
                  required
                  value={description}
                  onChange={(e) => setDescription(e.target.value)}
                  className="w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-red-500"
                  rows={3}
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">Recommended Treatment</label>
                <textarea
                  required
                  value={treatment}
                  onChange={(e) => setTreatment(e.target.value)}
                  className="w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-red-500"
                  rows={3}
                />
              </div>
              <div className="flex gap-2 justify-end">
                <button
                  type="button"
                  onClick={() => setShowForm(false)}
                  className="px-4 py-2 border rounded-md text-gray-600 hover:bg-gray-50"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="px-4 py-2 bg-red-600 hover:bg-red-700 text-white rounded-md font-semibold"
                >
                  Save
                </button>
              </div>
            </form>
          </div>
        )}

        {viewMode === 'users' ? (
          <div className="bg-white rounded-xl shadow-sm border overflow-hidden">
            <table className="min-w-full divide-y divide-gray-200">
              <thead className="bg-gray-50">
                <tr>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">ID</th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Name</th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Email</th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Role</th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Created At</th>
                </tr>
              </thead>
              <tbody className="bg-white divide-y divide-gray-200">
                {users.map((u) => (
                  <tr key={u.id}>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{u.id}</td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm font-semibold text-gray-900">{u.name}</td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{u.email}</td>
                    <td className="px-6 py-4 whitespace-nowrap">
                      <span className={`px-2 py-0.5 rounded-full text-xs font-medium ${
                        u.role === 'admin' ? 'bg-red-100 text-red-800' : 'bg-gray-100 text-gray-800'
                      }`}>
                        {u.role}
                      </span>
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                      {new Date(u.created_at).toLocaleDateString()}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        ) : (
          <div className="bg-white rounded-xl shadow-sm border overflow-hidden">
            <table className="min-w-full divide-y divide-gray-200">
              <thead className="bg-gray-50">
                <tr>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">ID</th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Name</th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Animal</th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Description</th>
                  <th className="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
                </tr>
              </thead>
              <tbody className="bg-white divide-y divide-gray-200">
                {diseases.map((d) => (
                  <tr key={d.id}>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{d.id}</td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm font-semibold text-gray-900">{d.name}</td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500 capitalize">{d.animal_type}</td>
                    <td className="px-6 py-4 text-sm text-gray-500 max-w-xs truncate">{d.description}</td>
                    <td className="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                      <button
                        onClick={() => handleEditClick(d)}
                        className="text-indigo-600 hover:text-indigo-900 mr-4"
                      >
                        <Edit2 size={16} className="inline mr-1" /> Edit
                      </button>
                      <button
                        onClick={() => handleDeleteDisease(d.id)}
                        className="text-red-600 hover:text-red-900"
                      >
                        <Trash2 size={16} className="inline mr-1" /> Delete
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
}
