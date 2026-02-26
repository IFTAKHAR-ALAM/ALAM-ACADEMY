#!/usr/bin/env python3
"""
Simple AI Book PDF Generator using ReportLab
Published by ALAM-ACADEMY
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.lib.colors import HexColor, lightblue
from reportlab.platypus import PageTemplate, BaseDocTemplate, Frame
from pathlib import Path
from datetime import datetime

def create_pdf():
    """Generate a PDF book."""
    
    output_path = Path(__file__).parent / 'AI_Comprehensive_Guide.pdf'
    
    # Get current date and time
    current_datetime = datetime.now().strftime("%B %d, %Y - %I:%M %p")
    
    styles = getSampleStyleSheet()
    
    doc = BaseDocTemplate(
        str(output_path),
        pagesize=A4,
        rightMargin=2.5*cm,
        leftMargin=2.5*cm,
        topMargin=3.5*cm,
        bottomMargin=2.5*cm
    )
    
    # Define frames for the page
    frame = Frame(
        doc.leftMargin,
        doc.bottomMargin,
        doc.width,
        doc.height,
        id='normal'
    )
    
    # Header style
    header_style = ParagraphStyle(
        'HeaderStyle',
        parent=styles['Normal'],
        fontSize=8,
        textColor=HexColor('#1e3a5f'),
        fontName='Helvetica'
    )
    
    def header_footer(canvas, doc):
        """Add header with light blue background and footer with page number."""
        # Save canvas state
        canvas.saveState()
        
        # Header with light blue background
        canvas.setFillColor(lightblue)
        canvas.rect(0, A4[1] - 2.5*cm, A4[0], 1*cm, fill=1, stroke=0)
        
        # Header text - using canvas.drawString directly
        canvas.setFont('Helvetica', 8)
        canvas.setFillColor(HexColor('#1e3a5f'))
        canvas.drawString(2.5*cm, A4[1] - 1.8*cm, f"ALAM-ACADEMY | AI Comprehensive Guide")
        canvas.drawRightString(A4[0] - 2.5*cm, A4[1] - 1.8*cm, f"Generated: {current_datetime}")
        
        # Footer with page number
        canvas.setFont('Helvetica', 8)
        canvas.setFillColor(HexColor('#666666'))
        canvas.drawCentredString(A4[0]/2, 1.5*cm, f"Page {doc.page}")
        
        # Restore canvas state
        canvas.restoreState()
    
    # Add page templates
    doc.addPageTemplates([
        PageTemplate(id='First', frames=frame, onPage=header_footer),
        PageTemplate(id='Later', frames=frame, onPage=header_footer),
    ])
    
    story = []
    
    # Custom styles
    title_style = ParagraphStyle(
        'AITitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=HexColor('#1e3a5f'),
        alignment=TA_CENTER,
        spaceAfter=30,
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'AISubtitle',
        parent=styles['Normal'],
        fontSize=12,
        textColor=HexColor('#4a5568'),
        alignment=TA_CENTER,
        spaceAfter=15,
        fontName='Helvetica'
    )
    
    heading_style = ParagraphStyle(
        'AIHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=HexColor('#2c5282'),
        spaceAfter=15,
        spaceBefore=20,
        fontName='Helvetica-Bold'
    )
    
    subheading_style = ParagraphStyle(
        'AISubheading',
        parent=styles['Heading3'],
        fontSize=13,
        textColor=HexColor('#2d3748'),
        spaceAfter=10,
        spaceBefore=15,
        fontName='Helvetica-Bold'
    )
    
    body_style = ParagraphStyle(
        'AIBody',
        parent=styles['Normal'],
        fontSize=11,
        textColor=HexColor('#1a1a1a'),
        spaceAfter=10,
        alignment=TA_JUSTIFY,
        fontName='Times-Roman',
        leading=16
    )
    
    info_style = ParagraphStyle(
        'AIInfo',
        parent=styles['Normal'],
        fontSize=11,
        textColor=HexColor('#1a202c'),
        spaceAfter=8,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    
    # === TITLE PAGE ===
    story.append(Spacer(1, 1.5*inch))
    story.append(Paragraph("COMPREHENSIVE GUIDE TO", subtitle_style))
    story.append(Paragraph("ARTIFICIAL INTELLIGENCE", title_style))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("Theory, Applications, Software & Hardware", subtitle_style))
    story.append(Paragraph("A Complete Guide for Students, Professionals, and Enthusiasts", subtitle_style))
    story.append(Spacer(1, 1*inch))
    story.append(Paragraph("Published by:", info_style))
    story.append(Paragraph("ALAM-ACADEMY", heading_style))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("Owner: M IFTIKHAR ALAM", info_style))
    story.append(Paragraph("Email: alammiftikhar@gmail.com", info_style))
    story.append(Paragraph("Contact: 0333-9257987", info_style))
    story.append(Paragraph("Address: Karachi, PAKISTAN", info_style))
    story.append(Paragraph("GitHub: https://github.com/IFTAKHAR-ALAM/ALAM-ACADEMY", info_style))
    story.append(Spacer(1, 0.8*inch))
    story.append(Paragraph("Copyright © 2026 ALAM-ACADEMY - All Rights Reserved", 
                          ParagraphStyle('Copyright', parent=styles['Normal'], fontSize=9, 
                                        textColor=HexColor('#666666'), alignment=TA_CENTER)))
    story.append(PageBreak())
    
    # === DEDICATION ===
    story.append(Spacer(1, 2*inch))
    story.append(Paragraph("DEDICATION", heading_style))
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph(
        "This book is dedicated to all the students, researchers, and professionals "
        "who are passionate about Artificial Intelligence and want to contribute to "
        "the advancement of this transformative technology for the benefit of humanity.",
        body_style
    ))
    story.append(PageBreak())
    
    # === PREFACE ===
    story.append(Paragraph("PREFACE", ParagraphStyle('ChapterTitle', parent=styles['Heading1'], 
                                                      fontSize=18, textColor=HexColor('#1e3a5f'))))
    story.append(Paragraph(
        "Artificial Intelligence (AI) has emerged as one of the most transformative technologies "
        "of the 21st century. From healthcare to finance, from transportation to entertainment, "
        "AI is reshaping every aspect of our lives. This comprehensive guide aims to provide "
        "readers with a thorough understanding of AI concepts, practical applications, software "
        "tools, and hardware requirements.",
        body_style
    ))
    story.append(Paragraph(
        "The book serves multiple audiences: students beginning their journey in AI, professionals "
        "looking to transition into AI careers, researchers seeking a comprehensive reference, "
        "business leaders wanting to understand AI implementation, and enthusiasts curious about "
        "this fascinating field.",
        body_style
    ))
    story.append(PageBreak())
    
    # === TABLE OF CONTENTS ===
    story.append(Paragraph("TABLE OF CONTENTS", heading_style))
    story.append(Spacer(1, 15))
    
    toc_entries = [
        "PART I: FOUNDATIONS OF ARTIFICIAL INTELLIGENCE",
        "  Chapter 1: Introduction to Artificial Intelligence ............ 1",
        "  Chapter 2: Mathematical Foundations for AI ................... 15",
        "  Chapter 3: Programming for AI ................................ 28",
        "",
        "PART II: MACHINE LEARNING FUNDAMENTALS",
        "  Chapter 4: Introduction to Machine Learning .................. 42",
        "  Chapter 5: Supervised Learning Algorithms .................... 55",
        "  Chapter 6: Unsupervised Learning Algorithms .................. 70",
        "  Chapter 7: Ensemble Methods and Advanced ML .................. 85",
        "",
        "PART III: DEEP LEARNING AND NEURAL NETWORKS",
        "  Chapter 8: Neural Networks Fundamentals ...................... 98",
        "  Chapter 9: Deep Learning Architectures ...................... 115",
        "  Chapter 10: Training Deep Neural Networks ................... 132",
        "",
        "PART IV: SPECIALIZED AI DOMAINS",
        "  Chapter 11: Natural Language Processing ..................... 148",
        "  Chapter 12: Computer Vision ................................. 168",
        "  Chapter 13: Speech and Audio Processing ..................... 185",
        "  Chapter 14: Robotics and Autonomous Systems ................. 198",
        "  Chapter 15: Reinforcement Learning .......................... 212",
        "",
        "PART V: AI SOFTWARE AND TOOLS",
        "  Chapter 16: AI Development Frameworks ....................... 228",
        "  Chapter 17: Data Science Tools for AI ....................... 245",
        "  Chapter 18: NLP Libraries and Tools ......................... 258",
        "  Chapter 19: Computer Vision Libraries ....................... 270",
        "  Chapter 20: MLOps and Deployment ............................ 282",
        "",
        "PART VI: AI HARDWARE",
        "  Chapter 21: Computing Hardware for AI ....................... 298",
        "  Chapter 22: Building AI Workstations ........................ 312",
        "  Chapter 23: Edge AI and IoT Hardware ........................ 325",
        "  Chapter 24: Cloud Infrastructure for AI ..................... 338",
        "",
        "PART VII: ADVANCED TOPICS",
        "  Chapter 25: Generative AI ................................... 352",
        "  Chapter 26: Explainable AI (XAI) ............................ 368",
        "  Chapter 27: AI Ethics and Responsible AI .................... 380",
        "  Chapter 28: AI Safety and Alignment ......................... 395",
        "",
        "PART VIII: INDUSTRY APPLICATIONS",
        "  Chapter 29: AI in Healthcare ................................ 408",
        "  Chapter 30: AI in Finance ................................... 422",
        "  Chapter 31: AI in Manufacturing ............................. 435",
        "  Chapter 32: AI in Retail and E-commerce ..................... 448",
        "  Chapter 33: AI in Transportation ............................ 460",
        "  Chapter 34: AI in Education ................................. 472",
        "",
        "PART IX: CAREER AND BUSINESS",
        "  Chapter 35: AI Career Paths ................................. 485",
        "  Chapter 36: Building AI Products ............................ 498",
        "  Chapter 37: AI Startup Guide ................................ 510",
        "",
        "PART X: FUTURE OF AI",
        "  Chapter 38: Emerging Trends in AI ........................... 525",
        "  Chapter 39: Artificial General Intelligence (AGI) ........... 538",
        "  Chapter 40: AI and the Future of Work ....................... 550",
        "",
        "APPENDICES .................................................... 565",
        "INDEX ......................................................... 620",
    ]
    
    for entry in toc_entries:
        if entry:
            story.append(Paragraph(entry, ParagraphStyle('TOC', parent=styles['Normal'], 
                                                          fontSize=10, leading=14)))
        else:
            story.append(Spacer(1, 8))
    
    story.append(PageBreak())
    
    # === CHAPTER 1 ===
    story.append(Paragraph("CHAPTER 1: INTRODUCTION TO ARTIFICIAL INTELLIGENCE", heading_style))
    
    story.append(Paragraph("1.1 What is Artificial Intelligence?", subheading_style))
    story.append(Paragraph(
        "Artificial Intelligence (AI) is a branch of computer science that aims to create "
        "intelligent machines capable of performing tasks that typically require human intelligence. "
        "These tasks include learning, reasoning, problem-solving, perception, understanding natural "
        "language, and even creativity.",
        body_style
    ))
    story.append(Paragraph(
        "AI can be defined as the simulation of human intelligence processes by machines, especially "
        "computer systems. These processes include learning (the acquisition of information and rules), "
        "reasoning (using rules to reach conclusions), self-correction (the ability to improve over "
        "time), perception (interpreting sensory input), and language understanding.",
        body_style
    ))
    
    story.append(Paragraph("1.2 History and Evolution of AI", subheading_style))
    story.append(Paragraph(
        "The journey of AI spans several decades, marked by periods of excitement, disappointment, "
        "and breakthrough discoveries. In 1950, Alan Turing published 'Computing Machinery and "
        "Intelligence,' proposing the Turing Test. The term 'Artificial Intelligence' was coined at "
        "the Dartmouth Conference in 1956.",
        body_style
    ))
    story.append(Paragraph(
        "The field experienced several 'AI winters' - periods of reduced funding and interest - but "
        "also remarkable breakthroughs. IBM's Deep Blue defeated chess champion Garry Kasparov in "
        "1997, and AlphaGo defeated Go champion Lee Sedol in 2016. The deep learning revolution "
        "beginning in 2012 has transformed the field, with Large Language Models emerging in recent "
        "years.",
        body_style
    ))
    
    story.append(Paragraph("1.3 Types of AI", subheading_style))
    story.append(Paragraph(
        "<b>Narrow AI (Weak AI):</b> Systems designed for specific tasks within a limited domain. "
        "Examples include virtual assistants (Siri, Alexa), recommendation systems (Netflix, Amazon), "
        "and image recognition systems. This is the most common form of AI today.",
        body_style
    ))
    story.append(Paragraph(
        "<b>General AI (Strong AI):</b> Hypothetical systems possessing human-level intelligence "
        "across all cognitive domains. AGI would be capable of learning any intellectual task a "
        "human can perform and transferring knowledge across domains. This remains theoretical.",
        body_style
    ))
    story.append(Paragraph(
        "<b>Superintelligence:</b> AI systems that would surpass human intelligence in all domains, "
        "including scientific creativity, general wisdom, and problem-solving abilities. This raises "
        "important ethical and safety considerations.",
        body_style
    ))
    
    story.append(Paragraph("1.4 AI vs Machine Learning vs Deep Learning", subheading_style))
    story.append(Paragraph(
        "<b>Artificial Intelligence (AI):</b> The broadest term encompassing any technique that "
        "enables computers to mimic human intelligence, including rule-based systems, expert systems, "
        "machine learning, robotics, and natural language processing.",
        body_style
    ))
    story.append(Paragraph(
        "<b>Machine Learning (ML):</b> A subset of AI focused on developing algorithms that learn "
        "patterns from data without being explicitly programmed. Types include supervised learning, "
        "unsupervised learning, and reinforcement learning.",
        body_style
    ))
    story.append(Paragraph(
        "<b>Deep Learning (DL):</b> A specialized subset of machine learning using artificial neural "
        "networks with multiple layers. It automatically learns feature representations and requires "
        "large amounts of data. Applications include image recognition, NLP, and autonomous vehicles.",
        body_style
    ))
    
    story.append(Paragraph("1.5 Applications of AI in Daily Life", subheading_style))
    story.append(Paragraph(
        "AI has become integral to modern life: email spam filtering, social media recommendations, "
        "streaming service suggestions (Netflix, Spotify), navigation apps (Google Maps), virtual "
        "assistants (Alexa, Google Home), healthcare diagnostics, banking fraud detection, and "
        "e-commerce product recommendations.",
        body_style
    ))
    
    story.append(Paragraph("1.6 Future of AI", subheading_style))
    story.append(Paragraph(
        "Near-term developments include more sophisticated generative AI, multimodal systems, edge "
        "AI processing, and increased regulation. Medium-term possibilities include widespread "
        "autonomous vehicles, personalized AI tutors, and AI-accelerated scientific discovery. "
        "Long-term possibilities include potential AGI development, brain-computer interfaces, and "
        "quantum AI systems.",
        body_style
    ))
    story.append(PageBreak())
    
    # === CHAPTER 2 ===
    story.append(Paragraph("CHAPTER 2: MATHEMATICAL FOUNDATIONS FOR AI", heading_style))
    
    story.append(Paragraph("2.1 Linear Algebra Essentials", subheading_style))
    story.append(Paragraph(
        "Linear algebra is the foundation of most AI and machine learning algorithms. Vectors are "
        "ordered lists of numbers representing points in space. Matrices are rectangular arrays of "
        "numbers used to represent datasets, neural network weights, and image data.",
        body_style
    ))
    story.append(Paragraph(
        "Key operations include vector addition, scalar multiplication, dot products, matrix "
        "multiplication, and transpose. Eigenvalues and eigenvectors are crucial for Principal "
        "Component Analysis (PCA). Matrix decompositions like SVD are fundamental for dimensionality "
        "reduction and recommendation systems.",
        body_style
    ))
    
    story.append(Paragraph("2.2 Calculus for Machine Learning", subheading_style))
    story.append(Paragraph(
        "Calculus provides tools for optimization, central to training ML models. Derivatives measure "
        "rates of change. The gradient (vector of partial derivatives) points in the direction of "
        "steepest increase. Gradient descent uses gradients to minimize loss functions.",
        body_style
    ))
    story.append(Paragraph(
        "The chain rule is essential for backpropagation in neural networks. Taylor series allow "
        "function approximation. Integration is used in probability calculations and expected value "
        "computation.",
        body_style
    ))
    
    story.append(Paragraph("2.3 Probability and Statistics", subheading_style))
    story.append(Paragraph(
        "Probability theory provides the framework for dealing with uncertainty. Bayes' Theorem "
        "enables updating beliefs with evidence and is the foundation of Naive Bayes classifiers. "
        "Random variables can be discrete or continuous, described by probability distributions.",
        body_style
    ))
    story.append(Paragraph(
        "Important distributions include Normal (Gaussian), Binomial, Poisson, and Uniform. Key "
        "statistical measures include mean (expected value), variance, standard deviation, covariance, "
        "and correlation. Hypothesis testing uses p-values to evaluate claims about populations.",
        body_style
    ))
    
    story.append(Paragraph("2.4 Optimization Techniques", subheading_style))
    story.append(Paragraph(
        "Gradient descent is the fundamental optimization algorithm: initialize parameters, compute "
        "gradients, update parameters in the opposite direction of the gradient, and repeat until "
        "convergence. Variants include batch gradient descent, stochastic gradient descent (SGD), "
        "and mini-batch gradient descent.",
        body_style
    ))
    story.append(Paragraph(
        "Advanced optimizers include Momentum (adds velocity to escape local minima), Adam (combines "
        "momentum with adaptive learning rates), and RMSprop (adapts learning rate per parameter). "
        "Convex optimization guarantees global minima for convex functions.",
        body_style
    ))
    
    story.append(Paragraph("2.5 Information Theory Basics", subheading_style))
    story.append(Paragraph(
        "Information theory quantifies information. Entropy measures uncertainty in a distribution - "
        "higher entropy means more uncertainty. Cross-entropy measures the difference between two "
        "distributions and is used as a loss function for classification.",
        body_style
    ))
    story.append(Paragraph(
        "Kullback-Leibler (KL) divergence measures how one distribution differs from another, used in "
        "Variational Autoencoders and model comparison. Mutual information measures dependency between "
        "variables, useful for feature selection.",
        body_style
    ))
    story.append(PageBreak())
    
    # === CHAPTER 3 ===
    story.append(Paragraph("CHAPTER 3: PROGRAMMING FOR AI", heading_style))
    
    story.append(Paragraph("3.1 Python for AI Development", subheading_style))
    story.append(Paragraph(
        "Python is the dominant language for AI development due to its simplicity, readability, and "
        "extensive ecosystem of libraries. Key features include dynamic typing, automatic memory "
        "management, and a vast standard library.",
        body_style
    ))
    story.append(Paragraph(
        "Python's syntax allows developers to focus on algorithms rather than low-level details. The "
        "language supports multiple programming paradigms including procedural, object-oriented, and "
        "functional programming.",
        body_style
    ))
    
    story.append(Paragraph("3.2 Essential Python Libraries", subheading_style))
    story.append(Paragraph(
        "<b>NumPy:</b> Fundamental package for numerical computing with support for arrays, matrices, "
        "and mathematical functions.",
        body_style
    ))
    story.append(Paragraph(
        "<b>Pandas:</b> Data manipulation and analysis library with DataFrames for structured data.",
        body_style
    ))
    story.append(Paragraph(
        "<b>Matplotlib/Seaborn:</b> Visualization libraries for creating charts, plots, and graphs.",
        body_style
    ))
    story.append(Paragraph(
        "<b>Scikit-learn:</b> Machine learning library with algorithms for classification, regression, "
        "clustering, and dimensionality reduction.",
        body_style
    ))
    story.append(Paragraph(
        "<b>TensorFlow/PyTorch:</b> Deep learning frameworks for building and training neural networks.",
        body_style
    ))
    
    story.append(Paragraph("3.3 Data Structures and Algorithms", subheading_style))
    story.append(Paragraph(
        "Understanding data structures is crucial for efficient AI implementations. Arrays and lists "
        "store sequences of data. Dictionaries (hash maps) provide fast key-value lookups. Sets enable "
        "efficient membership testing. Trees and graphs represent hierarchical and network data.",
        body_style
    ))
    story.append(Paragraph(
        "Algorithm complexity analysis (Big O notation) helps evaluate efficiency. Common complexities "
        "include O(1) constant, O(log n) logarithmic, O(n) linear, O(n log n) linearithmic, O(n²) "
        "quadratic, and O(2ⁿ) exponential.",
        body_style
    ))
    story.append(PageBreak())
    
    # === Add more chapter summaries ===
    chapters_overview = [
        ("CHAPTER 4: INTRODUCTION TO MACHINE LEARNING", 
         "Machine Learning enables computers to learn from data without explicit programming. "
         "Supervised learning uses labeled data for prediction tasks. Unsupervised learning finds "
         "patterns in unlabeled data. Reinforcement learning learns through interaction with an "
         "environment. The ML workflow includes data collection, preprocessing, model selection, "
         "training, evaluation, and deployment."),
        
        ("CHAPTER 5: SUPERVISED LEARNING ALGORITHMS",
         "Linear Regression predicts continuous values using linear relationships. Logistic Regression "
         "handles binary classification. Decision Trees make decisions through a tree-like model. "
         "Random Forests combine multiple trees for better accuracy. Support Vector Machines find "
         "optimal decision boundaries. k-Nearest Neighbors classifies based on similar examples. "
         "Naive Bayes uses probability for classification."),
        
        ("CHAPTER 6: UNSUPERVISED LEARNING ALGORITHMS",
         "Clustering groups similar data points. k-Means partitions data into k clusters. Hierarchical "
         "Clustering creates tree-like cluster structures. DBSCAN finds dense regions of points. "
         "Dimensionality reduction simplifies data while preserving information. PCA finds principal "
         "components that capture maximum variance. t-SNE and UMAP enable visualization of high-dimensional data."),
        
        ("CHAPTER 7: ENSEMBLE METHODS",
         "Ensemble methods combine multiple models for better performance. Bagging trains models "
         "independently on bootstrap samples. Boosting trains models sequentially, with each correcting "
         "previous errors. AdaBoost, Gradient Boosting, XGBoost, and LightGBM are popular boosting "
         "algorithms. Stacking combines predictions from multiple models using a meta-learner."),
        
        ("CHAPTER 8: NEURAL NETWORKS FUNDAMENTENTS",
         "Neural networks are inspired by biological neurons. Perceptrons are the simplest units. "
         "Multi-layer Perceptrons have hidden layers. Activation functions (ReLU, Sigmoid, Tanh) "
         "introduce non-linearity. Forward propagation computes predictions. Backpropagation calculates "
         "gradients for training. Loss functions measure prediction error. Optimizers update weights "
         "to minimize loss."),
        
        ("CHAPTER 9: DEEP LEARNING ARCHITECTURES",
         "Convolutional Neural Networks (CNNs) excel at image processing. Recurrent Neural Networks "
         "(RNNs) handle sequential data. LSTMs and GRUs address vanishing gradient problems. "
         "Autoencoders learn compressed representations. Generative Adversarial Networks (GANs) "
         "generate realistic data. Transformers use attention mechanisms for sequence processing, "
         "revolutionizing NLP."),
        
        ("CHAPTER 10: TRAINING DEEP NEURAL NETWORKS",
         "Data preprocessing includes normalization and augmentation. Weight initialization affects "
         "convergence. Batch Normalization stabilizes training. Dropout prevents overfitting. "
         "Hyperparameter tuning optimizes model performance. Transfer learning leverages pre-trained "
         "models. Model deployment serves predictions in production environments."),
    ]
    
    for chapter_title, content in chapters_overview:
        story.append(Paragraph(chapter_title, heading_style))
        story.append(Paragraph(content, body_style))
        story.append(Spacer(1, 15))
    
    story.append(PageBreak())
    
    # === AI Software Section ===
    story.append(Paragraph("PART V: AI SOFTWARE AND TOOLS - OVERVIEW", heading_style))
    
    story.append(Paragraph("TensorFlow", subheading_style))
    story.append(Paragraph(
        "Google's open-source platform for machine learning and deep learning. Provides flexible "
        "architecture for deployment across CPUs, GPUs, and TPUs. Includes Keras as a high-level API.",
        body_style
    ))
    
    story.append(Paragraph("PyTorch", subheading_style))
    story.append(Paragraph(
        "Facebook's deep learning framework known for dynamic computation graphs and Pythonic "
        "integration. Widely used in research and increasingly in production. Strong community support.",
        body_style
    ))
    
    story.append(Paragraph("Scikit-learn", subheading_style))
    story.append(Paragraph(
        "Comprehensive machine learning library for traditional ML algorithms. Includes tools for "
        "classification, regression, clustering, dimensionality reduction, and model selection.",
        body_style
    ))
    
    story.append(Paragraph("OpenCV", subheading_style))
    story.append(Paragraph(
        "Open Source Computer Vision library with over 2500 optimized algorithms. Used for image "
        "processing, object detection, facial recognition, and video analysis.",
        body_style
    ))
    
    story.append(Paragraph("Hugging Face Transformers", subheading_style))
    story.append(Paragraph(
        "Library providing thousands of pre-trained models for NLP tasks. Supports TensorFlow, PyTorch, "
        "and JAX. Enables easy use of BERT, GPT, and other transformer models.",
        body_style
    ))
    
    story.append(PageBreak())
    
    # === AI Hardware Section ===
    story.append(Paragraph("PART VI: AI HARDWARE - OVERVIEW", heading_style))
    
    story.append(Paragraph("GPUs (Graphics Processing Units)", subheading_style))
    story.append(Paragraph(
        "Parallel processors originally designed for graphics rendering, now essential for deep "
        "learning. NVIDIA's CUDA platform enables general-purpose GPU computing. Modern GPUs like "
        "A100 and H100 are optimized for AI workloads.",
        body_style
    ))
    
    story.append(Paragraph("TPUs (Tensor Processing Units)", subheading_style))
    story.append(Paragraph(
        "Google's custom-developed ASICs specifically designed for machine learning. Optimized for "
        "TensorFlow operations. Available through Google Cloud Platform for training and inference.",
        body_style
    ))
    
    story.append(Paragraph("Neural Processing Units (NPUs)", subheading_style))
    story.append(Paragraph(
        "Specialized processors designed for neural network operations. Found in modern smartphones "
        "and edge devices. Enable efficient on-device AI processing with low power consumption.",
        body_style
    ))
    
    story.append(Paragraph("FPGA and AI Accelerators", subheading_style))
    story.append(Paragraph(
        "Field-Programmable Gate Arrays offer customizable hardware for specific AI workloads. AI "
        "accelerator cards from Intel, AMD, and others provide alternatives to GPUs for inference.",
        body_style
    ))
    
    story.append(PageBreak())
    
    # === Industry Applications ===
    story.append(Paragraph("PART VIII: INDUSTRY APPLICATIONS - OVERVIEW", heading_style))
    
    story.append(Paragraph("AI in Healthcare", subheading_style))
    story.append(Paragraph(
        "Medical image analysis for diagnosis, drug discovery acceleration, personalized medicine, "
        "clinical decision support systems, and health monitoring through wearables. AI improves "
        "accuracy and efficiency in healthcare delivery.",
        body_style
    ))
    
    story.append(Paragraph("AI in Finance", subheading_style))
    story.append(Paragraph(
        "Fraud detection through anomaly identification, algorithmic trading, risk assessment, "
        "customer service chatbots, and regulatory compliance automation. AI enhances security and "
        "decision-making in financial services.",
        body_style
    ))
    
    story.append(Paragraph("AI in Manufacturing", subheading_style))
    story.append(Paragraph(
        "Predictive maintenance reduces downtime, quality control through computer vision, supply "
        "chain optimization, robotics automation, and digital twins for simulation. AI drives "
        "Industry 4.0 transformation.",
        body_style
    ))
    
    story.append(Paragraph("AI in Retail", subheading_style))
    story.append(Paragraph(
        "Recommendation systems personalize shopping, inventory management optimizes stock, customer "
        "analytics inform decisions, visual search enables image-based product discovery, and chatbots "
        "provide 24/7 customer service.",
        body_style
    ))
    
    story.append(PageBreak())
    
    # === Future of AI ===
    story.append(Paragraph("PART X: FUTURE OF AI - OVERVIEW", heading_style))
    
    story.append(Paragraph("Emerging Trends", subheading_style))
    story.append(Paragraph(
        "Quantum Machine Learning combines quantum computing with AI. Neuromorphic Computing mimics "
        "brain architecture. Federated Learning enables privacy-preserving distributed training. "
        "Self-Supervised Learning reduces labeling requirements. Multimodal AI processes multiple "
        "data types together.",
        body_style
    ))
    
    story.append(Paragraph("Artificial General Intelligence", subheading_style))
    story.append(Paragraph(
        "AGI represents human-level intelligence across all domains. Current approaches include "
        "scaling laws, multi-modal training, and cognitive architectures. Significant challenges "
        "remain in achieving true understanding and reasoning. Timeline predictions vary from decades "
        "to centuries.",
        body_style
    ))
    
    story.append(Paragraph("AI and the Future of Work", subheading_style))
    story.append(Paragraph(
        "Automation will transform job markets, displacing some roles while creating new ones. "
        "Human-AI collaboration will become standard. Reskilling and upskilling are essential. "
        "Society must address economic implications including potential need for Universal Basic "
        "Income.",
        body_style
    ))
    
    # === Publisher Page ===
    story.append(PageBreak())
    story.append(Paragraph("ABOUT THE PUBLISHER", heading_style))
    story.append(Spacer(1, 20))
    story.append(Paragraph(
        "<b>ALAM-ACADEMY</b> is a leading educational publisher based in Karachi, Pakistan, dedicated "
        "to providing high-quality educational materials in emerging technologies. Founded by "
        "M Iftikhar Alam, the academy focuses on making complex technical subjects accessible to "
        "students and professionals across South Asia and beyond.",
        body_style
    ))
    story.append(Spacer(1, 30))
    story.append(Paragraph("Contact Information:", subheading_style))
    story.append(Paragraph("Owner: M IFTIKHAR ALAM", info_style))
    story.append(Paragraph("Email: alammiftikhar@gmail.com", info_style))
    story.append(Paragraph("Phone: 0333-9257987", info_style))
    story.append(Paragraph("Address: Karachi, PAKISTAN", info_style))
    story.append(Paragraph("GitHub: https://github.com/IFTAKHAR-ALAM/ALAM-ACADEMY", info_style))
    
    # Build PDF
    print("Generating PDF...")
    doc.build(story)
    print(f"\n{'='*60}")
    print("PDF Generation Complete!")
    print(f"{'='*60}")
    print(f"Output file: {output_path}")
    print(f"Publisher: ALAM-ACADEMY")
    print(f"Owner: M IFTIKHAR ALAM")
    print(f"Contact: alammiftikhar@gmail.com | 0333-9257987")
    print(f"{'='*60}")

if __name__ == '__main__':
    create_pdf()
