<template>
  <div>
    <div class="col-sm-6 col-lg-3 px-2 mb-3">
      <!-- Team -->
      <div class="card h-100 transition-3d-hover">
        <div class="card-body">
          <div class="avatar avatar-lg avatar-circle mb-4">
            <img
              class="avatar-img"
              src="../../../static/img/committee/100x100/xiaojuan.png"
              alt="Image Description"
            />
          </div>

          <span class="d-block small font-weight-bold text-cap mb-1">{{
            $t("aboutus.VicePresident")
          }}</span>
          <a href="https://www.cse.ust.hk/~mxj/">
            <h4 class="text-lh-sm">Xiaojuan Ma</h4>
          </a>
          <p class="font-size-1">
            The Hong Kong University of Science and Technology
          </p>
        </div>
        <div class="card-footer border-0 pt-0">
          <!-- Social Networks -->
          <ul class="list-inline mb-0">
            <li class="list-inline-item">
              <a
                class="btn btn-xs btn-icon btn-soft-secondary rounded"
                href="#"
              >
                <i class="fab fa-facebook-f"></i>
              </a>
            </li>
            <li class="list-inline-item">
              <a
                class="btn btn-xs btn-icon btn-soft-secondary rounded"
                href="#"
              >
                <i class="fab fa-google"></i>
              </a>
            </li>
            <li class="list-inline-item">
              <a
                class="btn btn-xs btn-icon btn-soft-secondary rounded"
                href="#"
              >
                <i class="fab fa-twitter"></i>
              </a>
            </li>
          </ul>
          <!-- End Social Networks -->
        </div>
      </div>
      <!-- End Team -->
    </div>
  </div>
</template>