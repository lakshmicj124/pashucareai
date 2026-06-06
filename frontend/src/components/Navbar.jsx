import React, { useState } from "react";
import { Link, useNavigate, useLocation } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { useLanguage } from "../context/LanguageContext";
import { Menu, X, Globe, User, LogOut, ShieldAlert, Award, Compass, History, Settings, Home, MessageSquare, LayoutDashboard } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";

const Navbar = () => {
  const { user, logout } = useAuth();
  const { language, setLanguage, t } = useLanguage();
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const navigate = useNavigate();
  const location = useLocation();

  const handleLanguageToggle = () => {
    if (language === "en") {
      setLanguage("kn");
    } else if (language === "kn") {
      setLanguage("hi");
    } else {
      setLanguage("en");
    }
  };

  const navItems = [
    { name: t("home"), path: "/", icon: Home },
    ...(user && user.role !== "admin" ? [{ name: "Dashboard", path: "/dashboard", icon: LayoutDashboard }] : []),
    ...(user && user.role === "admin" ? [{ name: "Admin Panel", path: "/admin/dashboard", icon: ShieldAlert }] : []),
    { name: t("detect"), path: "/detect", icon: ShieldAlert },
    { name: t("chat"), path: "/chat", icon: MessageSquare },
    { name: t("vets"), path: "/vets", icon: Compass },
    ...(user ? [{ name: t("history"), path: "/history", icon: History }] : []),
    ...(user ? [{ name: t("settings"), path: "/settings", icon: Settings }] : []),
  ];

  const handleLogout = () => {
    logout();
    navigate("/");
  };

  return (
    <nav className="bg-slate-900 border-b border-slate-800 text-white sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo Section */}
          <Link to="/" className="flex items-center space-x-2">
            <span className="text-2xl font-bold bg-linear-to-r from-emerald-400 to-teal-500 bg-clip-text text-transparent flex items-center gap-2">
              🐄 <span className="hidden sm:inline font-extrabold">PashuCare AI</span>
            </span>
          </Link>

          {/* Desktop Navigation */}
          <div className="hidden md:flex items-center space-x-1">
            {navItems.map((item) => {
              const Icon = item.icon;
              const isActive = location.pathname === item.path;
              return (
                <Link
                  key={item.path}
                  to={item.path}
                  className={`flex items-center space-x-1 px-3 py-2 rounded-lg text-sm font-medium transition-all duration-200 ${
                    isActive
                      ? "bg-emerald-600 text-slate-50 shadow-lg shadow-emerald-600/30"
                      : "text-slate-300 hover:bg-slate-800 hover:text-white"
                  }`}
                >
                  <Icon className="w-4 h-4" />
                  <span>{item.name}</span>
                </Link>
              );
            })}
          </div>

          {/* Right Action buttons */}
          <div className="hidden md:flex items-center space-x-4">
            {/* Language Switcher */}
            <button
              onClick={handleLanguageToggle}
              className="flex items-center space-x-1 px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-850 hover:bg-slate-800 text-sm font-medium transition-all text-emerald-400"
            >
              <Globe className="w-4 h-4" />
              <span>
                {language === "en" ? "ಕನ್ನಡ" : language === "kn" ? "हिंदी" : "English"}
              </span>
            </button>

            {/* Auth Buttons */}
            {user ? (
              <div className="flex items-center space-x-4">
                <div className="flex items-center space-x-2 bg-slate-800 px-3 py-1.5 rounded-lg border border-slate-700">
                  <User className="w-4 h-4 text-emerald-400" />
                  <span className="text-sm font-medium text-slate-200">{user.name}</span>
                </div>
                <button
                  onClick={handleLogout}
                  className="flex items-center space-x-1 px-3 py-1.5 rounded-lg bg-red-650/80 hover:bg-red-650 border border-red-500/30 text-slate-50 text-sm font-semibold transition-all shadow-md shadow-red-900/30 cursor-pointer"
                >
                  <LogOut className="w-4 h-4" />
                  <span>{t("logout")}</span>
                </button>
              </div>
            ) : (
              <div className="flex items-center space-x-2">
                <Link
                  to="/login"
                  className="px-4 py-2 text-sm font-semibold text-slate-300 hover:text-white hover:bg-slate-800 rounded-lg transition-all"
                >
                  {t("login")}
                </Link>
                <Link
                  to="/register"
                  className="px-4 py-2 text-sm bg-linear-to-r from-emerald-500 to-teal-500 hover:from-emerald-600 hover:to-teal-600 rounded-lg transition-all shadow-md shadow-emerald-500/20 text-slate-900 font-extrabold"
                >
                  {t("register")}
                </Link>
              </div>
            )}
          </div>

          {/* Mobile menu button */}
          <div className="md:hidden flex items-center space-x-2">
            <button
              onClick={handleLanguageToggle}
              className="p-2 rounded-lg text-emerald-400 hover:bg-slate-800"
            >
              <Globe className="w-5 h-5" />
            </button>
            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="p-2 rounded-lg text-slate-400 hover:bg-slate-800 hover:text-white"
            >
              {mobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
            </button>
          </div>
        </div>
      </div>

      {/* Mobile Menu Panel */}
      <AnimatePresence>
        {mobileMenuOpen && (
          <motion.div
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: "auto" }}
            exit={{ opacity: 0, height: 0 }}
            className="md:hidden bg-slate-900 border-t border-slate-800 px-4 pt-2 pb-4 space-y-1"
          >
            {navItems.map((item) => {
              const Icon = item.icon;
              const isActive = location.pathname === item.path;
              return (
                <Link
                  key={item.path}
                  to={item.path}
                  onClick={() => setMobileMenuOpen(false)}
                  className={`flex items-center space-x-2 px-3 py-2.5 rounded-lg text-base font-medium transition-all ${
                    isActive ? "bg-emerald-600 text-slate-50" : "text-slate-300 hover:bg-slate-800 hover:text-white"
                  }`}
                >
                  <Icon className="w-5 h-5" />
                  <span>{item.name}</span>
                </Link>
              );
            })}

            <div className="pt-4 border-t border-slate-800 mt-4 space-y-2">
              {user ? (
                <>
                  <div className="px-3 py-2 text-sm text-slate-400 flex items-center space-x-2">
                    <User className="w-4 h-4 text-emerald-400" />
                    <span>{user.name} ({user.email})</span>
                  </div>
                  <button
                    onClick={() => {
                      setMobileMenuOpen(false);
                      handleLogout();
                    }}
                    className="w-full flex items-center space-x-2 px-3 py-2.5 rounded-lg bg-red-650/80 text-slate-50 text-base font-semibold"
                  >
                    <LogOut className="w-5 h-5" />
                    <span>{t("logout")}</span>
                  </button>
                </>
              ) : (
                <div className="grid grid-cols-2 gap-2">
                  <Link
                    to="/login"
                    onClick={() => setMobileMenuOpen(false)}
                    className="text-center py-2.5 rounded-lg text-slate-350 bg-slate-800 hover:bg-slate-750 font-semibold"
                  >
                    {t("login")}
                  </Link>
                  <Link
                    to="/register"
                    onClick={() => setMobileMenuOpen(false)}
                    className="text-center py-2.5 rounded-lg bg-linear-to-r from-emerald-500 to-teal-500 text-slate-900 font-extrabold"
                  >
                    {t("register")}
                  </Link>
                </div>
              )}
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </nav>
  );
};

export default Navbar;

