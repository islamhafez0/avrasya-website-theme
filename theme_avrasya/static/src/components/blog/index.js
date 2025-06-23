/** @odoo-module **/

import { Component, useState, onWillStart, useEffect } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { registry } from "@web/core/registry";

class LatestPosts extends Component {
  static template = "theme_avrasya.LatestPosts";
  setup() {
    this.state = useState({
      loading: true,
      error: null,
      latest_blogs: [],
    });
    onWillStart(async () => {
      await this.fetchLatestBlogs();
    });
    this.rpc = useService("rpc");
  }

  async fetchLatestBlogs() {
    try {
      this.loading = true;
      const response = await this.rpc("/api/blog/latest-posts");
      if (response) {
        const withCovers = response.map((post) => {
          let coverUrl = `/web/image/blog.post/${post.id}/website_image`;
          try {
            const props = JSON.parse(post.cover_properties || "{}");
            if (
              props["background-image"] &&
              props["background-image"] !== "none"
            ) {
              coverUrl = props["background-image"]
                .replace(/^url\(['"]?/, "")
                .replace(/['"]?\)$/, "");
            }
          } catch (error) {
            console.warn("bad cover_properties for post", post.id, error);
          }
          return {
            ...post,
            coverUrl,
            formattedDate: this.formatDate(post.post_date),
          };
        });
        this.state.latest_blogs = withCovers;
      } else {
        console.error("Error fetching blog data:", response.message);
      }
    } catch (error) {
      this.state.error = "Something went wrong, please try again!";
      console.error(error);
    } finally {
      this.state.loading = false;
    }
  }
  formatDate(dateStr) {
    const date = new Date(dateStr);
    const options = { year: "numeric", month: "long", day: "numeric" };
    return date.toLocaleDateString("en-US", options);
  }
}
registry
  .category("public_components")
  .add("theme_avrasya.LatestPosts", LatestPosts);
