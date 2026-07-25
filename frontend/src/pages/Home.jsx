import { Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export default function Home() {
  const { isAuthenticated } = useAuth();

  return (
    <div className="flex flex-col items-center justify-center min-h-[80vh] text-center px-4">
      <h1 className="text-4xl font-bold text-slate-900 mb-3">
        RemoteCareer AI
      </h1>
      <p className="text-slate-600 max-w-md mb-6">
        AI-powered career guidance for online and distance education students.
      </p>
      <Link
        to={isAuthenticated ? "/profile" : "/signup"}
        className="bg-slate-900 hover:bg-slate-800 text-white px-6 py-3 rounded-md"
      >
        {isAuthenticated ? "Go to your profile" : "Get started"}
      </Link>
    </div>
  );
}