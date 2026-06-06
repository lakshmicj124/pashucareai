import React, { useState, useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { ShieldCheck, Mail, Lock, ArrowRight, AlertCircle } from "lucide-react";
import { motion } from "framer-motion";

const AdminLogin = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [submitError, setSubmitError] = useState("");
  const { login, user, loading, error, clearError } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    clearError();
  }, [email, password]);

  useEffect(() => {
    if (user && user.role === "admin") {
      navigate("/admin/dashboard");
    } else if (user && user.role !== "admin") {
      navigate("/dashboard");
    }
  }, [user, navigate]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setSubmitError("");
    const result = await login(email, password);
    if (!result.success) {
      setSubmitError(result.error || "Admin Login failed. Please check credentials.");
    }
  };

  return (
    <div className="min-h-screen bg-slate-950 flex flex-col justify-center py-12 sm:px-6 lg:px-8 relative overflow-hidden">
      <div className="absolute inset-0 bg-center mask-[linear-gradient(180deg,white,rgba(255,255,255,0))] opacity-20"></div>

      <div className="sm:mx-auto sm:w-full sm:max-w-md relative z-10">
        <motion.div
          initial={{ y: -20, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          className="flex justify-center"
        >
          <div className="w-16 h-16 rounded-2xl bg-linear-to-br from-emerald-400 to-cyan-500 p-0.5 shadow-lg shadow-emerald-500/30">
            <div className="w-full h-full bg-slate-900 rounded-2xl flex items-center justify-center">
              <ShieldCheck className="w-8 h-8 text-emerald-400" />
            </div>
          </div>
        </motion.div>

        <motion.h2
          initial={{ y: 20, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ delay: 0.1 }}
          className="mt-6 text-center text-3xl font-bold tracking-tight text-white"
        >
          Admin Portal
        </motion.h2>
        <motion.p
          initial={{ y: 20, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ delay: 0.2 }}
          className="mt-2 text-center text-sm text-slate-400"
        >
          Sign in to manage the PashuCare AI platform
        </motion.p>
      </div>

      <motion.div
        initial={{ y: 20, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        transition={{ delay: 0.3 }}
        className="mt-8 sm:mx-auto sm:w-full sm:max-w-md relative z-10"
      >
        <div className="bg-slate-900/80 backdrop-blur-xl py-8 px-4 shadow-2xl shadow-emerald-900/20 sm:rounded-2xl sm:px-10 border border-slate-800">

          {(error || submitError) && (
            <motion.div
              initial={{ opacity: 0, height: 0 }}
              animate={{ opacity: 1, height: "auto" }}
              className="mb-6 bg-red-500/10 border border-red-500/50 rounded-xl p-4 flex items-start space-x-3"
            >
              <AlertCircle className="w-5 h-5 text-red-400 shrink-0 mt-0.5" />
              <p className="text-sm text-red-400">{error || submitError}</p>
            </motion.div>
          )}

          <form className="space-y-6" onSubmit={handleSubmit}>
            <div>
              <label className="block text-sm font-medium text-slate-300">Admin Email</label>
              <div className="mt-2 relative rounded-xl shadow-sm">
                <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                  <Mail className="h-5 w-5 text-slate-500" />
                </div>
                <input
                  type="email"
                  required
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  className="block w-full pl-10 bg-slate-800/50 border border-slate-700 rounded-xl py-3 text-white placeholder-slate-500 focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-all"
                  placeholder="admin@example.com"
                />
              </div>
            </div>

            <div>
              <label className="block text-sm font-medium text-slate-300">Password</label>
              <div className="mt-2 relative rounded-xl shadow-sm">
                <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                  <Lock className="h-5 w-5 text-slate-500" />
                </div>
                <input
                  type="password"
                  required
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  className="block w-full pl-10 bg-slate-800/50 border border-slate-700 rounded-xl py-3 text-white placeholder-slate-500 focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-all"
                  placeholder="••••••••"
                />
              </div>
            </div>

            <button
              type="submit"
              disabled={loading}
              className="group relative w-full flex justify-center py-3 px-4 border border-transparent text-sm font-semibold rounded-xl text-slate-900 bg-linear-to-r from-emerald-400 to-cyan-500 hover:from-emerald-300 hover:to-cyan-400 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-emerald-500 focus:ring-offset-slate-900 transition-all disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {loading ? (
                <div className="w-5 h-5 border-2 border-slate-900 border-t-transparent rounded-full animate-spin" />
              ) : (
                <>
                  Secure Login
                  <ArrowRight className="ml-2 h-5 w-5 group-hover:translate-x-1 transition-transform" />
                </>
              )}
            </button>
          </form>

          <div className="mt-6 text-center">
            <Link to="/login" className="text-sm font-medium text-emerald-400 hover:text-emerald-300 transition-colors">
              Return to User Login
            </Link>
          </div>
        </div>
      </motion.div>
    </div>
  );
};

export default AdminLogin;

