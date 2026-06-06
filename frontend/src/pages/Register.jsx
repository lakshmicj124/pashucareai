import React, { useState, useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { useLanguage } from "../context/LanguageContext";
import { User, Lock, Mail, Phone, AlertCircle, ArrowRight } from "lucide-react";
import { motion } from "framer-motion";

const Register = () => {
  const { register, error, clearError } = useAuth();
  const { t } = useLanguage();
  const navigate = useNavigate();

  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [phone, setPhone] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [localError, setLocalError] = useState("");
  const [isSuccess, setIsSuccess] = useState(false);

  useEffect(() => {
    if (clearError) clearError();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLocalError("");

    if (!name || !email || !phone || !password || !confirmPassword) {
      setLocalError("Please fill in all fields.");
      return;
    }

    // Email validation
    const emailRegex = /^[\w\.-]+@[\w\.-]+\.\w+$/;
    if (!emailRegex.test(email)) {
      setLocalError("Please enter a valid email address.");
      return;
    }

    // Phone validation (+91 or 10 digits)
    const phoneRegex = /^(\+91[\-\s]?)?[0-9]{10}$/;
    if (!phoneRegex.test(phone)) {
      setLocalError("Please enter a valid 10-digit phone number (optionally prefixed with +91).");
      return;
    }

    // Password validation (min 8 chars, at least one special char)
    if (password.length < 8) {
      setLocalError("Password must be at least 8 characters long.");
      return;
    }

    const specialCharRegex = /[!@#$%^&*(),.?":{}|<>_]/;
    if (!specialCharRegex.test(password)) {
      setLocalError("Password must include at least one special character.");
      return;
    }

    // Confirm password check
    if (password !== confirmPassword) {
      setLocalError("Passwords do not match.");
      return;
    }

    setLoading(true);
    const result = await register(name, email, phone, password);
    setLoading(false);

    if (result.success) {
      navigate("/dashboard");
    }
  };

  return (
    <div className="bg-slate-950 min-h-[calc(100vh-4rem)] flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
      <motion.div
        initial={{ opacity: 0, scale: 0.95 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.3 }}
        className="max-w-md w-full space-y-8 bg-slate-900 border border-slate-800 p-8 rounded-2xl shadow-xl shadow-black/40"
      >
        <div className="text-center">
          <span className="text-4xl">🐄</span>
          <h2 className="mt-4 text-3xl font-extrabold text-white">{t("register")}</h2>
          <p className="mt-2 text-sm text-slate-400">
            Create your account to start managing livestock health
          </p>
        </div>

        <form className="mt-8 space-y-6" onSubmit={handleSubmit}>
          {(error || localError) && (
            <div className="bg-red-500/10 border border-red-500/30 rounded-xl p-4 flex items-center space-x-3 text-red-400 text-sm">
              <AlertCircle className="w-5 h-5 shrink-0" />
              <span>{localError || error}</span>
            </div>
          )}

          <div className="space-y-4">
            <div>
              <label className="block text-sm font-semibold text-slate-300 mb-2">
                {t("fullName")}
              </label>
              <div className="relative">
                <span className="absolute inset-y-0 left-0 pl-3 flex items-center text-slate-500">
                  <User className="w-5 h-5" />
                </span>
                <input
                  type="text"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  className="block w-full pl-10 pr-3 py-3 border border-slate-700 rounded-xl bg-slate-950 text-white placeholder-slate-550 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500 transition-all text-sm"
                  placeholder="Ravi Kumar"
                  required
                />
              </div>
            </div>

            <div>
              <label className="block text-sm font-semibold text-slate-300 mb-2">
                {t("email")}
              </label>
              <div className="relative">
                <span className="absolute inset-y-0 left-0 pl-3 flex items-center text-slate-500">
                  <Mail className="w-5 h-5" />
                </span>
                <input
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  className="block w-full pl-10 pr-3 py-3 border border-slate-700 rounded-xl bg-slate-950 text-white placeholder-slate-550 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500 transition-all text-sm"
                  placeholder="farmer@example.com"
                  required
                />
              </div>
            </div>

            <div>
              <label className="block text-sm font-semibold text-slate-300 mb-2">
                Phone Number
              </label>
              <div className="relative">
                <span className="absolute inset-y-0 left-0 pl-3 flex items-center text-slate-500">
                  <Phone className="w-5 h-5" />
                </span>
                <input
                  type="tel"
                  value={phone}
                  onChange={(e) => setPhone(e.target.value)}
                  className="block w-full pl-10 pr-3 py-3 border border-slate-700 rounded-xl bg-slate-950 text-white placeholder-slate-550 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500 transition-all text-sm"
                  placeholder="+91 9876543210"
                  required
                />
              </div>
            </div>

            <div>
              <label className="block text-sm font-semibold text-slate-300 mb-2">
                {t("password")}
              </label>
              <div className="relative">
                <span className="absolute inset-y-0 left-0 pl-3 flex items-center text-slate-500">
                  <Lock className="w-5 h-5" />
                </span>
                <input
                  type="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  className="block w-full pl-10 pr-3 py-3 border border-slate-700 rounded-xl bg-slate-950 text-white placeholder-slate-550 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500 transition-all text-sm"
                  placeholder="••••••••"
                  required
                />
              </div>
            </div>

            <div>
              <label className="block text-sm font-semibold text-slate-300 mb-2">
                Confirm Password
              </label>
              <div className="relative">
                <span className="absolute inset-y-0 left-0 pl-3 flex items-center text-slate-500">
                  <Lock className="w-5 h-5" />
                </span>
                <input
                  type="password"
                  value={confirmPassword}
                  onChange={(e) => setConfirmPassword(e.target.value)}
                  className="block w-full pl-10 pr-3 py-3 border border-slate-700 rounded-xl bg-slate-950 text-white placeholder-slate-550 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500 transition-all text-sm"
                  placeholder="••••••••"
                  required
                />
              </div>
            </div>
          </div>

          <button
            type="submit"
            disabled={loading}
            className="w-full flex items-center justify-center space-x-2 bg-linear-to-r from-emerald-500 to-teal-500 hover:from-emerald-600 hover:to-teal-600 text-slate-950 font-extrabold py-3 px-4 rounded-xl shadow-lg shadow-emerald-500/20 transition-all cursor-pointer"
          >
            {loading ? (
              <div className="animate-spin rounded-full h-5 w-5 border-t-2 border-slate-950"></div>
            ) : (
              <>
                <span>{t("register")}</span>
                <ArrowRight className="w-5 h-5" />
              </>
            )}
          </button>
        </form>

        <div className="text-center pt-2">
          <Link
            to="/login"
            className="text-sm font-semibold text-emerald-450 hover:text-emerald-400 hover:underline"
          >
            {t("alreadyHaveAccount")}
          </Link>
        </div>
      </motion.div>
    </div>
  );
};

export default Register;

