import { resolve } from "path";
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import windicss from "vite-plugin-windicss";

export default defineConfig({
  plugins: [vue(), windicss()],
  server: { port: 8080 },
  resolve: {
    alias: [{ find: "@", replacement: resolve(__dirname, "src") }],
  },
  build: { chunkSizeWarningLimit: 600, cssCodeSplit: false },
});
