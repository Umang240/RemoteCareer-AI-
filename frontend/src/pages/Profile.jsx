import { useEffect, useState } from "react";
import { apiClient, getErrorMessage } from "../api/client";

const emptyForm = {
  name: "",
  email: "",
  education: "",
  skills: "",
  target_role: "",
};

export default function Profile() {
  const [profile, setProfile] = useState(null); // null = no profile yet
  const [loading, setLoading] = useState(true);
  const [editing, setEditing] = useState(false);
  const [form, setForm] = useState(emptyForm);
  const [error, setError] = useState("");
  const [saving, setSaving] = useState(false);

  useEffect(() => {
    fetchProfile();
  }, []);

  async function fetchProfile() {
    setLoading(true);
    setError("");
    try {
      const response = await apiClient.get("/profile/me");
      setProfile(response.data);
    } catch (err) {
      if (err.response?.status === 404) {
        // No profile yet — that's expected for a new user.
        setProfile(null);
      } else {
        setError(getErrorMessage(err));
      }
    } finally {
      setLoading(false);
    }
  }

  function startEditing() {
    if (profile) {
      setForm({
        name: profile.name,
        email: profile.email,
        education: profile.education,
        skills: profile.skills.join(", "),
        target_role: profile.target_role,
      });
    } else {
      setForm(emptyForm);
    }
    setError("");
    setEditing(true);
  }

  async function handleSubmit(e) {
    e.preventDefault();
    setError("");
    setSaving(true);

    const payload = {
      name: form.name,
      email: form.email,
      education: form.education,
      skills: form.skills
        .split(",")
        .map((s) => s.trim())
        .filter(Boolean),
      target_role: form.target_role,
    };

    try {
      if (profile) {
        await apiClient.put(`/update-profile/${profile._id}`, payload);
      } else {
        await apiClient.post("/create-profile", payload);
      }
      await fetchProfile();
      setEditing(false);
    } catch (err) {
      setError(getErrorMessage(err));
    } finally {
      setSaving(false);
    }
  }

  async function handleDelete() {
    if (!profile) return;
    if (!confirm("Delete your profile? This can't be undone.")) return;

    setError("");
    try {
      await apiClient.delete(`/delete-profile/${profile._id}`);
      setProfile(null);
    } catch (err) {
      setError(getErrorMessage(err));
    }
  }

  if (loading) {
    return <p className="text-center mt-16 text-slate-500">Loading...</p>;
  }

  return (
    <div className="max-w-xl mx-auto mt-10 px-4">
      <h1 className="text-2xl font-semibold text-slate-900 mb-6">
        Your Profile
      </h1>

      {error && (
        <div className="bg-red-50 text-red-700 text-sm px-3 py-2 rounded-md mb-4">
          {error}
        </div>
      )}

      {!editing && profile && (
        <div className="bg-white shadow-md rounded-lg p-6 space-y-3">
          <Field label="Name" value={profile.name} />
          <Field label="Email" value={profile.email} />
          <Field label="Education" value={profile.education} />
          <Field label="Skills" value={profile.skills.join(", ")} />
          <Field label="Target Role" value={profile.target_role} />

          <div className="flex gap-3 pt-2">
            <button
              onClick={startEditing}
              className="bg-slate-900 hover:bg-slate-800 text-white px-4 py-2 rounded-md text-sm"
            >
              Edit
            </button>
            <button
              onClick={handleDelete}
              className="bg-red-600 hover:bg-red-700 text-white px-4 py-2 rounded-md text-sm"
            >
              Delete
            </button>
          </div>
        </div>
      )}

      {!editing && !profile && (
        <div className="bg-white shadow-md rounded-lg p-6 text-center space-y-4">
          <p className="text-slate-600">
            You haven't created a profile yet.
          </p>
          <button
            onClick={startEditing}
            className="bg-slate-900 hover:bg-slate-800 text-white px-4 py-2 rounded-md text-sm"
          >
            Create Profile
          </button>
        </div>
      )}

      {editing && (
        <form
          onSubmit={handleSubmit}
          className="bg-white shadow-md rounded-lg p-6 space-y-4"
        >
          <TextInput
            label="Name"
            value={form.name}
            onChange={(v) => setForm({ ...form, name: v })}
            required
          />
          <TextInput
            label="Email"
            type="email"
            value={form.email}
            onChange={(v) => setForm({ ...form, email: v })}
            required
          />
          <TextInput
            label="Education"
            value={form.education}
            onChange={(v) => setForm({ ...form, education: v })}
            required
          />
          <TextInput
            label="Skills (comma separated)"
            value={form.skills}
            onChange={(v) => setForm({ ...form, skills: v })}
            placeholder="Python, React, MongoDB"
            required
          />
          <TextInput
            label="Target Role"
            value={form.target_role}
            onChange={(v) => setForm({ ...form, target_role: v })}
            required
          />

          <div className="flex gap-3 pt-2">
            <button
              type="submit"
              disabled={saving}
              className="bg-slate-900 hover:bg-slate-800 text-white px-4 py-2 rounded-md text-sm disabled:opacity-50"
            >
              {saving ? "Saving..." : "Save"}
            </button>
            <button
              type="button"
              onClick={() => setEditing(false)}
              className="bg-slate-100 hover:bg-slate-200 text-slate-700 px-4 py-2 rounded-md text-sm"
            >
              Cancel
            </button>
          </div>
        </form>
      )}
    </div>
  );
}

function Field({ label, value }) {
  return (
    <div>
      <p className="text-xs uppercase tracking-wide text-slate-400">
        {label}
      </p>
      <p className="text-slate-900">{value}</p>
    </div>
  );
}

function TextInput({ label, value, onChange, type = "text", placeholder, required }) {
  return (
    <div>
      <label className="block text-sm font-medium text-slate-700 mb-1">
        {label}
      </label>
      <input
        type={type}
        required={required}
        value={value}
        placeholder={placeholder}
        onChange={(e) => onChange(e.target.value)}
        className="w-full border border-slate-300 rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-slate-900"
      />
    </div>
  );
}