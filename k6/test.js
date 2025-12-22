import http from "k6/http";
import { check, sleep } from "k6";

export const options = {
  vus: 2,
  duration: "30s",
  thresholds: {
    http_req_failed: ["rate==0"],
    http_req_duration: ["p(95)<500"],
  },
};

export default function () {
  const res = http.get("https://test.k6.io");

  check(res, {
    "status is 200": r => r.status === 200,
    "response < 500ms": r => r.timings.duration < 500,
  });

  sleep(1);
}

