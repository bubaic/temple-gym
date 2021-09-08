<template>
  <div class="h-screen flex flex-row flex-wrap">
    <DashboardNavbar :isSidebarOpen="isOpen" />
    <DashboardSidebar :isSidebarOpen="isOpen" />
  </div>
</template>

<script>
  import DashboardNavbar from "@/layouts/navigation/dashboard/Navbar.vue";
  import DashboardSidebar from "@/layouts/navigation/dashboard/Sidebar.vue";

  export default {
    components: { DashboardNavbar, DashboardSidebar },
    data: function () {
      return { isOpen: false };
    },
    methods: {
      toggleSidebar: function () {
        this.isOpen = !this.isOpen;
      },
    },
  };
</script>

<style scoped></style>
