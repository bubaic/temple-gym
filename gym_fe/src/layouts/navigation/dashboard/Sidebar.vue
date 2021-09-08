<template>
  <div class="sidebar" v-if="isOpen">
    <div class="wrapper">
      <span class="brand">temple gym</span>

      <p class="sidebar__head">dashboards</p>
      <a href="./index.html" class="sidebar__link">
        <i class="fad fa-chart-pie"></i>
        <span>analytics</span>
      </a>

      <a href="./index-1.html" class="sidebar__link">
        <i class="fad fa-shopping-cart text-xs mr-2"></i>
        <span>shop</span>
      </a>

      <p class="sidebar__head">apps</p>
      <a href="#" class="sidebar__link">
        <i class="fad fa-envelope-open-text"></i>
        <span>email</span>
      </a>

      <a href="#" class="sidebar__link">
        <i class="fad fa-comments"></i>
        <span>chat</span>
      </a>

      <a href="#" class="sidebar__link">
        <i class="fad fa-shield-check"></i>
        <span>todo</span>
      </a>

      <a href="#" class="sidebar__link">
        <i class="fad fa-calendar-edit"></i>
        <span>calendar</span>
      </a>

      <p class="sidebar__head">reports</p>
      <a href="#" class="sidebar__link">
        <i class="fad fa-file-invoice-dollar"></i>
        <span>invoice</span>
      </a>
    </div>
  </div>
</template>

<script>
  export default {
    name: "sidebar",
    props: ["isOpen"],
  };
</script>

<style lang="scss" scoped>
  @import "@/assets/styles/reusable";

  @layer base {
    .wrapper {
      @extend %flexColumn;
      align-items: start !important;

      .brand {
        @apply font-poppins font-bold capitalize text-lg mb-4 text-gray-700;
      }
    }

    .sidebar {
      @extend %trans;
      @apply relative flex-wrap w-52 flex-none p-5 overflow-y-scroll
        md:fixed md:top-0 md:z-30 md:h-screen md:shadow-xl
			  border-r border-gray-300 bg-light-500;
      // md:-ml-64 ;

      &__head {
        @apply uppercase text-xs text-blue-gray-400 mb-4
				font-poppins font-semibold tracking-wider;

        &:not(:first-child) {
          @apply mt-4;
        }
      }
      &__link {
        @extend %trans;
        @apply mb-2 capitalize font-medium text-sm
				text-gray-600 hover:text-brand-primary;
      }
    }

    .fad {
      @apply text-xs mr-2 relative -top-px;
    }
  }
</style>
