<template>
  <div class="dashboard">
    <DashboardNavbar :isSidebarOpen="isOpen" @toggleSidebar="toggle" />

    <div class="h-screen flex flex-1">
      <DashboardSidebar :isSidebarOpen="isOpen" />
      <ContentArea class="h-full overflow-y-auto" />
    </div>
  </div>
</template>

<script>
import DashboardNavbar from "@/components/navigation/topnav/Navbar.vue";
import DashboardSidebar from "@/components/navigation/sidenav/Sidebar.vue";
import ContentArea from "./MainContent.vue";

export default {
  components: { ContentArea, DashboardNavbar, DashboardSidebar },
  data: function () {
    return { isOpen: false };
  },
  methods: {
    toggle: function () {
      this.isOpen = !this.isOpen;
    },
  },
};
</script>

<style scoped>
.dashboard {
  /* @apply flex flex-col w-full h-screen bg-brand; */
  @apply w-full bg-brand;
}
</style>
