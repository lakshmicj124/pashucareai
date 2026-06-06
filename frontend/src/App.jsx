import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { AuthProvider } from "./context/AuthContext";
import { LanguageProvider } from "./context/LanguageContext";
import { ThemeProvider } from "./context/ThemeContext";
import ProtectedRoute from "./components/ProtectedRoute";
import AdminProtectedRoute from "./components/AdminProtectedRoute";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";

// Import Pages
import Home from "./pages/Home";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Detect from "./pages/Detect";
import NearbyVets from "./pages/NearbyVets";
import History from "./pages/History";
import Settings from "./pages/Settings";
import Chatbot from "./pages/Chatbot";
import Dashboard from "./pages/Dashboard";
import AdminLogin from "./pages/AdminLogin";
import AdminDashboard from "./pages/AdminDashboard";

// Styling
import "./App.css";

function App() {
  return (
    <Router>
      <ThemeProvider>
        <LanguageProvider>
          <AuthProvider>
            <div className="flex flex-col min-h-screen bg-slate-950 text-white selection:bg-emerald-500 selection:text-slate-950 font-sans">
              {/* Navigation Header */}
              <Navbar />

            {/* Main Content Area */}
            <main className="grow">
              <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/login" element={<Login />} />
                <Route path="/register" element={<Register />} />
                <Route path="/vets" element={<NearbyVets />} />
                <Route path="/admin/login" element={<AdminLogin />} />
                
                {/* Protected Routes */}
                <Route
                  path="/dashboard"
                  element={
                    <ProtectedRoute>
                      <Dashboard />
                    </ProtectedRoute>
                  }
                />
                <Route
                  path="/detect"
                  element={
                    <ProtectedRoute>
                      <Detect />
                    </ProtectedRoute>
                  }
                />
                <Route
                  path="/history"
                  element={
                    <ProtectedRoute>
                      <History />
                    </ProtectedRoute>
                  }
                />
                <Route
                  path="/chat"
                  element={
                    <ProtectedRoute>
                      <Chatbot />
                    </ProtectedRoute>
                  }
                />
                <Route
                  path="/settings"
                  element={
                    <ProtectedRoute>
                      <Settings />
                    </ProtectedRoute>
                  }
                />

                {/* Admin Routes */}
                <Route
                  path="/admin/dashboard"
                  element={
                    <AdminProtectedRoute>
                      <AdminDashboard />
                    </AdminProtectedRoute>
                  }
                />
              </Routes>
            </main>

            {/* Footer */}
            <Footer />
          </div>
        </AuthProvider>
      </LanguageProvider>
    </ThemeProvider>
  </Router>
  );
}

export default App;

