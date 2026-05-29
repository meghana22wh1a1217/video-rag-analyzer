"use client";

import { useState } from "react";

export default function Home() {
  const [videoA, setVideoA] = useState("");
  const [videoB, setVideoB] = useState("");
  const [response, setResponse] = useState("");

  const processVideos = async () => {
    try {
      setResponse("Processing videos...");

      const res = await fetch(
        "http://127.0.0.1:8000/analyze",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            video_a: videoA,
            video_b: videoB,
          }),
        }
      );

      const data = await res.json();

      setResponse(JSON.stringify(data, null, 2));
    } catch (error) {
      console.error(error);
      setResponse("Backend connection failed");
    }
  };

  return (
    <main className="min-h-screen bg-gray-100 p-8">
      <div className="max-w-6xl mx-auto">

        <h1 className="text-4xl font-bold mb-8 text-center">
          Video RAG Analyzer
        </h1>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

          {/* Left Panel */}
          <div className="bg-white p-6 rounded-xl shadow">

            <h2 className="text-2xl font-semibold mb-4">
              Compare Videos
            </h2>

            <label className="block mb-2 font-medium">
              Video A URL
            </label>

            <input
              type="text"
              value={videoA}
              onChange={(e) => setVideoA(e.target.value)}
              placeholder="Paste YouTube or Instagram URL"
              className="w-full border p-3 rounded mb-4"
            />

            <label className="block mb-2 font-medium">
              Video B URL
            </label>

            <input
              type="text"
              value={videoB}
              onChange={(e) => setVideoB(e.target.value)}
              placeholder="Paste YouTube or Instagram URL"
              className="w-full border p-3 rounded mb-6"
            />

            <button
              onClick={processVideos}
              className="w-full bg-blue-600 text-white p-3 rounded hover:bg-blue-700"
            >
              Process Videos
            </button>

          </div>

          {/* Right Panel */}
          <div className="bg-white p-6 rounded-xl shadow">

            <h2 className="text-2xl font-semibold mb-4">
              Chat Assistant
            </h2>

            <div className="border h-96 p-4 rounded overflow-auto whitespace-pre-wrap">
              {response || "Chat responses will appear here..."}
            </div>

          </div>

        </div>
      </div>
    </main>
  );
}