from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ALB 직접 연결 방식을 쓸 경우를 대비해 CORS 설정 추가 (선택 사항이지만 권장)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # 실제 운영시에는 도메인을 특정하는게 좋음
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/status")
async def get_status():
    return {
        "status": "Healthy",
        "deploy_target": "EC2 via Docker Compose",
        "version": "1.0.1"
    }