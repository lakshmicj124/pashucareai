import React, { createContext, useState, useContext, useEffect } from "react";
import axios from "axios";

// Create custom API client instance
export const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(() => localStorage.getItem("pashucare_token"));
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Set default auth headers whenever token changes
  useEffect(() => {
    if (token) {
      localStorage.setItem("pashucare_token", token);
      api.defaults.headers.common["Authorization"] = `Bearer ${token}`;
      fetchUserProfile();
    } else {
      localStorage.removeItem("pashucare_token");
      delete api.defaults.headers.common["Authorization"];
      setUser(null);
      setLoading(false);
    }
  }, [token]);

  const fetchUserProfile = async () => {
    try {
      setLoading(true);
      const res = await api.get("/api/auth/me");
      setUser(res.data);
      setError(null);
    } catch (err) {
      console.error("Failed to load user profile:", err);
      logout();
    } finally {
      setLoading(false);
    }
  };

  const login = async (email, password) => {
    try {
      setLoading(true);
      setError(null);
      const res = await api.post("/api/auth/login", { email, password });
      setToken(res.data.token);
      setUser(res.data.user);
      return { success: true };
    } catch (err) {
      const msg = err.response?.data?.detail || "Login failed. Please check credentials.";
      setError(msg);
      return { success: false, error: msg };
    } finally {
      setLoading(false);
    }
  };

  const register = async (name, email, phone_number, password) => {
    try {
      setLoading(true);
      setError(null);
      const res = await api.post("/api/auth/register", { name, email, phone_number, password });
      setToken(res.data.token);
      setUser(res.data.user);
      return { success: true };
    } catch (err) {
      const msg = err.response?.data?.detail || "Registration failed. Try again.";
      setError(msg);
      return { success: false, error: msg };
    } finally {
      setLoading(false);
    }
  };

  const logout = () => {
    setToken(null);
    setUser(null);
  };

  const clearError = () => {
    setError(null);
  };

  return (
    <AuthContext.Provider value={{ user, setUser, token, loading, error, login, register, logout, clearError }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
