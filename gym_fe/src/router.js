import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    /* mains */
    // { path: "/", component: () => import("@/pages/Main") },
    {
      path: "/:notfound(.*)",
      component: () => import("@/pages/errors/404.vue"),
    },
    // { path: "/shop", component: () => import("@/pages/Shop") },

    /* account */
    // { path: "/login", component: () => import("@/pages/Login") },
    // { path: "/sign-up", component: () => import("@/pages/Signup") },

    /* dashboard */
    {
      path: "/dashboard",
      component: () => import("@/pages/admin/Dashboard.vue"),
    },

    /* company */
    { path: "/", component: () => import("@/pages/Home.vue") },
    { path: "/about", component: () => import("@/pages/About.vue") },

    /* membership */

    /* quicklink */

    /* section: nested */
  ],
});

export { router };
