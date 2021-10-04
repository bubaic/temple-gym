<template>
  <nav class="navbar">
    <div class="nav-container">
      <div class="logo">temple gym</div>

      <ul class="navbar__menu">
        <li>
          <button
            class="notify"
            @click="toggleNotifyMenu"
            @keydown.esc="closeNotifyMenu"
            aria-label="Notifications"
            aria-haspopup="true"
          >
            <tg-icon name="notify" class="w-5 h-5" aria-hidden="true" />
            <span aria-hidden="true" class="notify--badge"></span>
          </button>

          <NotificationMenu :isNotifyOpened="notifyOpened" />
        </li>

        <li>
          <button
            class="profile"
            @click="toggleProfileMenu"
            @keydown.esc="closeProfileMenu"
            aria-label="Account"
            aria-haspopup="true"
          >
            <img
              class="profile__img"
              src="../../../assets/img/u1.jpg"
              aria-hidden="true"
            />
          </button>

          <transition enter-class="transition duration-150 ease-in">
            <ProfileMenu :isSubmenuOpened="submenuOpened" />
          </transition>
        </li>

        <li>
          <button class="menu" aria-label="Menu" @click="toggleSidebarMenu">
            <a class="hamburger" :class="{ opened: !isSidebarOpen }">
              <span>click to {{ !isSidebarOpen ? 'close' : 'open' }} sidebar</span>
            </a>
          </button>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
import "@/components/icons/notify";
import ProfileMenu from "./NavProfileItem.vue";
import NotificationMenu from "./NotificationMenu.vue";

export default {
  props: ["isSidebarOpen"],
  emits: ["toggleSidebar"],
  components: { NotificationMenu, ProfileMenu },
  data: function () {
    return {
      submenuOpened: false,
      notifyOpened: false,
    };
  },
  methods: {
    toggleProfileMenu: function () {
      this.submenuOpened = !this.submenuOpened;
      if (this.submenuOpened) this.notifyOpened = false;
    },
    closeProfileMenu: function () {
      this.submenuOpened = false;
    },
    toggleNotifyMenu: function () {
      this.notifyOpened = !this.notifyOpened;
      if (this.notifyOpened) this.submenuOpened = false;
    },
    closeNotifyMenu: function () {
      this.notifyOpened = false;
    },
    toggleSidebarMenu: function () {
      this.$emit("toggleSidebar");
    },
  },
};
</script>

<style lang="scss" scoped>
@import "@/assets/styles/reusable";

.navbar {
  @apply z-10 py-4 shadow bg-warm-gray-100;

  .nav-container {
    @extend %flexRow;
    @apply h-full px-6 container mx-auto;
  }

  .logo {
    @apply capitalize font-bold font-poppins;
  }

  &__menu {
    @extend %flexRow;
    @apply flex items-center space-x-3 ml-auto;

    & > li {
      @apply relative;
    }
  }

  .notify,
  .profile {
    @apply align-middle rounded-full focus:outline-none p-0.5;
  }
  .notify {
    &--badge {
      @apply absolute top-0 right-0 inline-block w-3 h-3 rounded-full
        bg-red-600 border-2 border-warm-gray-100;
    }
  }
  .profile {
    @apply focus:ring-2 focus:ring-brand-secondary shadow-xl;

    &__img {
      @apply object-cover w-8 h-8 rounded-full;
    }
  }
}

.menu {
  @apply relative cursor-pointer focus:outline-none;
}
.hamburger {
  @extend %trans;
  @apply w-5 h-1 -top-1 rounded-md block cursor-pointer relative
   bg-brand-secondary;

  &::before,
  &::after {
    content: "";
    @apply absolute w-7 h-1 rounded-md outline-none left-0
      bg-brand-secondary;
  }

  &::before {
    @apply -top-2;
  }
  &::after {
    @apply top-2;
  }

  span {
    @apply absolute top-6 -right-1 w-24 px-2 py-1 shadow-md text-sm hidden
      rounded font-pt text-blue-gray-600 bg-blue-gray-100 text-left;
  }

  &:hover {
    span {
      @apply block
    }
  }
}
.opened {
  @apply bg-transparent;

  &::before {
    @extend %trans;
    @apply transform -rotate-45 top-0;
  }
  &::after {
    @extend %trans;
    @apply transform rotate-45 top-0;
  }
}
</style>
