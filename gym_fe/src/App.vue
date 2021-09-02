<template>
  <div class="bg">
    <!-- <r> -->
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/about"> About</RouterLink>
      <RouterLink to="/dashboard"> Dashboard</RouterLink>
    <router-view></router-view>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
#app {
  background: #e9f5fe;
  p {
    @apply bg-light-800 p-2;
  }
}
</style>
