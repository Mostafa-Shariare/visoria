import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(14, 7))

# Hide axes
ax.axis('off')

# Box 1: Edge Client
rect1 = patches.FancyBboxPatch((0.05, 0.15), 0.25, 0.65, boxstyle="round,pad=0.03", edgecolor='#4f46e5', facecolor='#eef2ff', lw=2)
ax.add_patch(rect1)
ax.text(0.175, 0.75, "1. Student Edge Client\n(100% Local Processing)", ha='center', va='center', fontsize=13, fontweight='bold', color='#1e1b4b')
ax.text(0.175, 0.65, "• Webcam Capture", ha='center', va='center', fontsize=11)
ax.text(0.175, 0.55, "• MediaPipe (Facial/Hands)", ha='center', va='center', fontsize=11)
ax.text(0.175, 0.45, "• YOLOv8n (Phone Object)", ha='center', va='center', fontsize=11)
ax.text(0.175, 0.35, "• Feature Engineering (23 Signals)", ha='center', va='center', fontsize=11)
ax.text(0.175, 0.25, "• Random Forest Classifier", ha='center', va='center', fontsize=11)
ax.text(0.175, 0.18, "• 15-Frame Temporal Smoother", ha='center', va='center', fontsize=11)

# Arrow 1 to 2
ax.annotate('', xy=(0.38, 0.45), xytext=(0.32, 0.45), arrowprops=dict(arrowstyle="->", lw=2.5, color="#64748b"))
ax.text(0.35, 0.50, "JSON Telemetry\n(WebSockets)", ha='center', va='center', fontsize=10, color="#475569", fontweight='bold')

# Box 2: Backend
rect2 = patches.FancyBboxPatch((0.38, 0.15), 0.25, 0.65, boxstyle="round,pad=0.03", edgecolor='#d946ef', facecolor='#fdf4ff', lw=2)
ax.add_patch(rect2)
ax.text(0.505, 0.75, "2. Centralized Backend\n(FastAPI Server)", ha='center', va='center', fontsize=13, fontweight='bold', color='#4a044e')
ax.text(0.505, 0.60, "• WebSocket Broadcaster", ha='center', va='center', fontsize=11)
ax.text(0.505, 0.50, "• Live Session Aggregation", ha='center', va='center', fontsize=11)
ax.text(0.505, 0.40, "• Distraction Alert Engine", ha='center', va='center', fontsize=11)
ax.text(0.505, 0.30, "• Socratic API & Analytics", ha='center', va='center', fontsize=11)
ax.text(0.505, 0.20, "• MongoDB Storage", ha='center', va='center', fontsize=11)

# Arrow 2 to 3
ax.annotate('', xy=(0.71, 0.45), xytext=(0.65, 0.45), arrowprops=dict(arrowstyle="->", lw=2.5, color="#64748b"))
ax.text(0.68, 0.50, "Live Broadcast\n& HTTP", ha='center', va='center', fontsize=10, color="#475569", fontweight='bold')

# Box 3: Frontend
rect3 = patches.FancyBboxPatch((0.71, 0.15), 0.25, 0.65, boxstyle="round,pad=0.03", edgecolor='#14b8a6', facecolor='#f0fdfa', lw=2)
ax.add_patch(rect3)
ax.text(0.835, 0.75, "3. Interactive Web Portals\n(React 19 + Vite)", ha='center', va='center', fontsize=13, fontweight='bold', color='#042f2e')
ax.text(0.835, 0.60, "• Live Teacher Dashboard", ha='center', va='center', fontsize=11)
ax.text(0.835, 0.50, "• Attention Heatmaps", ha='center', va='center', fontsize=11)
ax.text(0.835, 0.40, "• Launch Socratic Intervention", ha='center', va='center', fontsize=11)
ax.text(0.835, 0.30, "• Student Reflection UI", ha='center', va='center', fontsize=11)
ax.text(0.835, 0.20, "• Historical Analytics Export", ha='center', va='center', fontsize=11)

plt.title("Visoria End-to-End System Pipeline", fontsize=18, fontweight='bold', pad=30, color='#0f172a')
plt.tight_layout()
plt.savefig("d:/Capstone/Project_testing/system_pipeline_slide.png", dpi=300, bbox_inches='tight')
print("Diagram saved to d:/Capstone/Project_testing/system_pipeline_slide.png")
