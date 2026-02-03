import axios from "axios";

const API_BASE = process.env.REACT_APP_API_BASE || "http://localhost:8000/api";

const api = axios.create({
  baseURL: API_BASE,
  headers: {
    "Content-Type": "application/json",
    "X-API-KEY": process.env.REACT_APP_API_KEY || "changeme",
  },
});

export async function queryChat(query: string, top_k = 5) {
  const resp = await api.post("/chat/query", { query, top_k });
  return resp.data;
}

// WebSocket chat placeholder
export function createChatSocket(onMessage) {
  const wsUrl = (process.env.REACT_APP_WS_URL || "ws://localhost:8000") + "/ws";
  const ws = new WebSocket(wsUrl);
  ws.onmessage = (ev) => onMessage(JSON.parse(ev.data));
  return ws;
}
