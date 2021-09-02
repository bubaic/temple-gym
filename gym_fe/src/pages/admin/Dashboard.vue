<template>
  <div class="h-screen flex flex-row flex-wrap">
    <DashboardNavbar />
    <DashboardSidebar />
  </div>
</template>

<script>
import DashboardNavbar from "@/layouts/navigation/dashboard/Navbar.vue";
import DashboardSidebar from "@/layouts/navigation/dashboard/Sidebar.vue";

export default {
  components: { DashboardNavbar, DashboardSidebar },
};
</script>

<style scoped></style>
