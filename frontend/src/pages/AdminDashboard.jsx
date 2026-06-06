import React, { useEffect, useState } from "react";
import { useAuth, api } from "../context/AuthContext";
import { API_BASE_URL } from "../services/api";
import { Users, Activity, MessageSquare, AlertTriangle, Shield, CheckCircle } from "lucide-react";
import { motion } from "framer-motion";

const AdminDashboard = () => {
  const { user } = useAuth();
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const res = await api.get("/api/admin/dashboard");
        setStats(res.data);
      } catch (err) {
        setError("Failed to load admin statistics.");
      } finally {
        setLoading(false);
      }
    };
    fetchStats();
  }, []);

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center pt-20">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-emerald-500"></div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen pt-24 px-6 max-w-7xl mx-auto text-center text-red-400">
        <AlertTriangle className="w-12 h-12 mx-auto mb-4" />
        <p>{error}</p>
      </div>
    );
  }

  return (
    <div className="min-h-screen pt-24 pb-12 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto">
      <div className="flex items-center justify-between mb-8">
        <div>
          <h1 className="text-3xl font-bold text-white flex items-center gap-3">
            <Shield className="w-8 h-8 text-emerald-400" />
            Admin Dashboard
          </h1>
          <p className="text-slate-400 mt-2">Welcome back, {user?.name}</p>
        </div>
        <div className="flex items-center gap-2 px-4 py-2 bg-emerald-500/10 border border-emerald-500/20 rounded-full text-emerald-400">
          <CheckCircle className="w-4 h-4" />
          <span className="text-sm font-medium">System Online</span>
        </div>
      </div>

      {/* Stats Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
        <motion.div
          initial={{ y: 20, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          className="bg-slate-900/50 backdrop-blur-sm border border-slate-800 p-6 rounded-2xl"
        >
          <div className="flex items-center justify-between">
            <div>
              <p className="text-slate-400 text-sm font-medium">Total Users</p>
              <h3 className="text-3xl font-bold text-white mt-2">{stats.statistics.total_users}</h3>
            </div>
            <div className="w-12 h-12 rounded-full bg-blue-500/20 flex items-center justify-center">
              <Users className="w-6 h-6 text-blue-400" />
            </div>
          </div>
        </motion.div>

        <motion.div
          initial={{ y: 20, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ delay: 0.1 }}
          className="bg-slate-900/50 backdrop-blur-sm border border-slate-800 p-6 rounded-2xl"
        >
          <div className="flex items-center justify-between">
            <div>
              <p className="text-slate-400 text-sm font-medium">Total Detections</p>
              <h3 className="text-3xl font-bold text-white mt-2">{stats.statistics.total_detections}</h3>
            </div>
            <div className="w-12 h-12 rounded-full bg-emerald-500/20 flex items-center justify-center">
              <Activity className="w-6 h-6 text-emerald-400" />
            </div>
          </div>
        </motion.div>

        <motion.div
          initial={{ y: 20, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ delay: 0.2 }}
          className="bg-slate-900/50 backdrop-blur-sm border border-slate-800 p-6 rounded-2xl"
        >
          <div className="flex items-center justify-between">
            <div>
              <p className="text-slate-400 text-sm font-medium">Chatbot Conversations</p>
              <h3 className="text-3xl font-bold text-white mt-2">{stats.statistics.total_chatbot_conversations}</h3>
            </div>
            <div className="w-12 h-12 rounded-full bg-purple-500/20 flex items-center justify-center">
              <MessageSquare className="w-6 h-6 text-purple-400" />
            </div>
          </div>
        </motion.div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        {/* Recent Users */}
        <div className="bg-slate-900/50 backdrop-blur-sm border border-slate-800 rounded-2xl overflow-hidden">
          <div className="p-6 border-b border-slate-800">
            <h3 className="text-lg font-bold text-white">Recent Users</h3>
          </div>
          <div className="divide-y divide-slate-800">
            {stats.recent_users.map((u, idx) => (
              <div key={u._id || idx} className="p-4 px-6 flex items-center justify-between hover:bg-slate-800/50 transition-colors">
                <div>
                  <p className="text-white font-medium">{u.name}</p>
                  <p className="text-sm text-slate-400">{u.email}</p>
                </div>
                <div className="text-xs font-medium px-2 py-1 bg-slate-800 rounded text-slate-300">
                  {new Date(u.created_at).toLocaleDateString()}
                </div>
              </div>
            ))}
            {stats.recent_users.length === 0 && (
              <div className="p-6 text-center text-slate-400">No recent users.</div>
            )}
          </div>
        </div>

        {/* Recent Detections */}
        <div className="bg-slate-900/50 backdrop-blur-sm border border-slate-800 rounded-2xl overflow-hidden">
          <div className="p-6 border-b border-slate-800">
            <h3 className="text-lg font-bold text-white">Recent Detections</h3>
          </div>
          <div className="divide-y divide-slate-800">
            {stats.recent_detections.map((d, idx) => (
              <div key={idx} className="p-4 px-6 flex items-center justify-between hover:bg-slate-800/50 transition-colors">
                <div className="flex items-center gap-4">
                  <div className="w-10 h-10 rounded-lg bg-slate-800 overflow-hidden">
                    {d.image_url ? (
                      <img src={`${API_BASE_URL}${d.image_url}`} alt="Detection" className="w-full h-full object-cover" />
                    ) : (
                      <div className="w-full h-full flex items-center justify-center text-slate-500">?</div>
                    )}
                  </div>
                  <div>
                    <p className="text-white font-medium">{d.disease_name}</p>
                    <p className="text-sm text-slate-400">{d.animal_type}</p>
                  </div>
                </div>
                <div className="text-xs font-medium px-2 py-1 bg-slate-800 rounded text-slate-300">
                  {new Date(d.timestamp).toLocaleDateString()}
                </div>
              </div>
            ))}
            {stats.recent_detections.length === 0 && (
              <div className="p-6 text-center text-slate-400">No recent detections.</div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default AdminDashboard;

