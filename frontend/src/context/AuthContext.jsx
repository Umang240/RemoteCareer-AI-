import { createContext, useContext, useState } from "react";
import { apiClient, getErrorMessage } from "../api/client";

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [token, setToken] = useState(() => localStorage.getItem("access_token"));

  const isAuthenticated = Boolean(token);

  async function login(email, password) {
    try {
      const response = await apiClient.post("/auth/login", { email, password });
      // API returns an envelope: { success, message, data }
      const access_token = response.data?.data?.access_token;
      if (!access_token) {
        return { success: false, message: response.data?.message || "Authentication failed" };
      }
      localStorage.setItem("access_token", access_token);
      setToken(access_token);
      return { success: true };
    } catch (error) {
      return { success: false, message: getErrorMessage(error) };
    }
  }

  async function signup(name, email, password) {
    try {
      await apiClient.post("/auth/signup", { name, email, password });
      return { success: true };
    } catch (error) {
      return { success: false, message: getErrorMessage(error) };
    }
  }

  function logout() {
    localStorage.removeItem("access_token");
    setToken(null);
  }

  return (
    <AuthContext.Provider value={{ token, isAuthenticated, login, signup, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error("useAuth must be used within an AuthProvider");
  }
  return context;
}