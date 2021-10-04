<template>
  <p class="sidebar__head">{{ header }}</p>
  <a
    href="./index.html"
    class="sidebar__link"
    v-for="(c, idx) in content"
    :key="idx"
  >
    <i :class="`fad fa-${c.icon}`" />
    <span>{{ c.title }}</span>
  </a>
</template>

<script>
  export default { props: ["header", "content"] };
</script>

<style lang="scss" scoped>
  .sidebar__head {
    @apply uppercase text-xs text-true-gray-500 mt-4 mb-2
	font-poppins font-semibold tracking-wider;

    &:first-of-type {
      @apply mt-8;
    }
  }
  .sidebar__link {
    @apply mb-1 capitalize font-medium text-sm font-pt
	text-blue-gray-600 hover:text-brand-primary
    focus:text-brand-primary;
  }
</style>
